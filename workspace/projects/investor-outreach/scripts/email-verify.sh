#!/bin/bash
# Email Domain Verification Script
# Extracts unique domains from the CSV, checks MX records, outputs results

CSV="/data/.openclaw/workspace/projects/investor-outreach/MASTER-investor-database-v2.csv"
DOMAIN_RESULTS="/tmp/domain_mx_results.csv"

# Extract unique domains from email column (column 2)
# Handle malformed emails (multiple emails separated by comma) by taking the first one
echo "domain,has_mx,mx_records,resolves" > "$DOMAIN_RESULTS"

# Extract all email-like strings from column 2, get domains
awk -F',' '{
  # Column 2 is the email field - but CSV may have quoted fields
  # Simple approach: get field 2
  email=$2
  # Remove quotes
  gsub(/"/, "", email)
  # Skip header
  if (NR == 1) next
  # Skip empty
  if (email == "") next
  # Take first email if multiple (some have comma-separated emails in quoted field)
  split(email, parts, ",")
  for (i in parts) {
    e = parts[i]
    gsub(/^ +| +$/, "", e)
    if (index(e, "@") > 0) {
      split(e, ep, "@")
      domain = ep[2]
      gsub(/^ +| +$/, "", domain)
      if (domain != "") print domain
    }
  }
}' "$CSV" | sort -u > /tmp/unique_domains.txt

echo "Found $(wc -l < /tmp/unique_domains.txt) unique domains"

# Check MX records for each domain
while IFS= read -r domain; do
  # Skip empty
  [ -z "$domain" ] && continue
  
  # Check MX records
  mx_output=$(dig +short MX "$domain" 2>/dev/null)
  
  if [ -n "$mx_output" ]; then
    # Has MX records
    mx_clean=$(echo "$mx_output" | tr '\n' '; ' | sed 's/; $//')
    echo "$domain,yes,\"$mx_clean\",yes"
  else
    # No MX - check if domain resolves at all (A record)
    a_output=$(dig +short A "$domain" 2>/dev/null)
    if [ -n "$a_output" ]; then
      echo "$domain,no,,yes"
    else
      # Check if NXDOMAIN
      dig_status=$(dig "$domain" +short 2>/dev/null)
      nxdomain=$(dig "$domain" 2>/dev/null | grep -c "NXDOMAIN")
      if [ "$nxdomain" -gt 0 ]; then
        echo "$domain,no,,dead"
      else
        echo "$domain,no,,maybe"
      fi
    fi
  fi
done < /tmp/unique_domains.txt >> "$DOMAIN_RESULTS"

echo "MX check complete. Results in $DOMAIN_RESULTS"
wc -l "$DOMAIN_RESULTS"
