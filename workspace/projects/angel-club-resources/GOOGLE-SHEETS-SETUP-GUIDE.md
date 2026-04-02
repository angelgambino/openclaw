# Google Sheets Setup Guide — Angel Club Public Resources
## Making it searchable, filterable, and professional

After importing the .xlsx, follow these steps in Google Sheets:

---

## 1. DATA VALIDATION DROPDOWNS

### Sector Focus (Investors + Angels tabs)
The sector data uses "/" separators. To make it filterable:

**Option A: Use Filter Views (RECOMMENDED — easiest)**
1. Select all data → Data → Create a filter
2. Click the filter arrow on "Sector Focus" column
3. Users can search/filter by typing keywords
4. This already works with the auto-filter in the .xlsx

**Option B: Add a Search/Filter row at top**
1. Insert a row at Row 2 (below headers)
2. In the Sector Focus cell, add Data Validation → List from a range
3. Create a hidden "Sectors" sheet with all unique sectors listed
4. Users select from dropdown to filter

### Stage Dropdown
Add Data Validation to the "Stage" column:
- List of items: `Pre-Seed, Seed, Series A, Series B, Growth, All Stages`
- This standardizes entries and enables clean filtering

### Type Dropdown (Investors tab)
Add Data Validation to the "Type" column:
- List of items: `VC, CVC, Family Office`

### Type Dropdown (Angels tab)
- List of items: `Individual Angel, Angel Group, Syndicate`

### Lead/Follow Dropdown
- List of items: `Lead, Follow, Both, Unknown`

### Application Type Dropdown
- List of items: `Open Application, Warm Intro Recommended, Referral Only, Accelerator Program`

---

## 2. MAKING IT SEARCHABLE

### Method 1: Filter Views (Built-in, no setup needed)
The .xlsx already has auto-filters on every tab. Users can:
- Click any column header filter arrow
- Search by text
- Sort A-Z or Z-A
- Filter by condition

### Method 2: Add a SEARCH Tab (Power User)
Create a new tab called "🔍 Search" with these features:

**Cell A1:** "Search by Sector"
**Cell B1:** Dropdown with all sectors

**Cell A2:** "Search by Stage" 
**Cell B2:** Dropdown: Pre-Seed / Seed / Series A / All

**Cell A3:** "Search by Location"
**Cell B3:** Dropdown with regions: US / Europe / Asia / LATAM / Africa / Middle East / Global

**Cell A5 onwards:** Use FILTER formula:
```
=FILTER(Investors!A:P, 
  ISNUMBER(SEARCH(B1, Investors!C:C)),
  ISNUMBER(SEARCH(B2, Investors!D:D)),
  ISNUMBER(SEARCH(B3, Investors!E:E))
)
```

This creates a live search that pulls matching investors based on the dropdowns.

### Method 3: Slicer (Google Sheets native)
1. Select data range on any tab
2. Data → Add a slicer
3. Choose column (Sector Focus, Stage, Location, Type)
4. A floating filter button appears
5. Users click to filter visually

**Recommended: Add slicers for Sector, Stage, Location, and Type on the Investors and Angels tabs.**

---

## 3. PROTECT FROM COPYING

After importing:
1. File → Share → Share with others
2. Set to "Anyone with the link can VIEW"
3. Click the gear icon (⚙️) in the share dialog
4. UNCHECK "Editors can change permissions and share"
5. CHECK "Viewers and commenters can see the option to download, print, and copy" → set to OFF

**Additional protection:**
- Tools → Protect sheet → Protect entire workbook
- Only you (owner) can edit
- Viewers can only view + use filters

---

## 4. CONDITIONAL FORMATTING FOR DEADLINES

On tabs with deadlines (Competitions, Grants, Fellowships, Events, Demo Days):

1. Select the deadline column
2. Format → Conditional formatting
3. Add rules:
   - **Red background** → Custom formula: `=AND(A2<>"", A2<TODAY()+7, A2>=TODAY())` (due within 7 days)
   - **Yellow background** → Custom formula: `=AND(A2<>"", A2<TODAY()+30, A2>=TODAY()+7)` (due within 30 days)
   - **Gray background** → Custom formula: `=AND(A2<>"", A2<TODAY())` (expired)
   - **Green background** → Custom formula: `=AND(A2<>"", A2>=TODAY()+30)` (30+ days out)

---

## 5. TAB COLORS

After import, set tab colors to match Angel Club branding:
- Right-click each tab → Change color
- Investor tabs: Navy/Dark Blue
- Program tabs (Accelerators, Studios, Incubators): Teal
- Opportunity tabs (Competitions, Grants, Events): Green
- Knowledge tabs (Books, Newsletters, Blogs, Podcasts): Purple
- Tool tabs (Tools, Databases): Orange
- Start Here + Credits: Gold/accent color

---

## 6. MOBILE OPTIMIZATION

Google Sheets on mobile is limited but:
- Frozen headers work ✅
- Filters work ✅
- Slicers work ✅
- Recommend adding the sheet to the Google Sheets app for best mobile experience
- Consider creating a companion Notion or Airtable view for better mobile UX later

---

## QUICK SETUP CHECKLIST

- [ ] Import .xlsx into Google Sheets
- [ ] Verify all 18 tabs imported correctly
- [ ] Set sharing to View Only
- [ ] Disable download/print/copy for viewers
- [ ] Add slicers on Investors + Angels tabs (Sector, Stage, Location, Type)
- [ ] Add conditional formatting for deadline columns
- [ ] Set tab colors
- [ ] Test filter views
- [ ] Share link on angelclub.com/resources page
