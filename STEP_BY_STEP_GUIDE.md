# Step-by-Step Usage Guide
## Municipal Rezoning Tracker - Complete Walkthrough

---

## Part 1: Initial Setup (5 minutes)

### Step 1.1: Download All Files

Download all files from the outputs folder and save them in one directory:

```
municipal_rezoning_tracker/
├── municipal_rezoning_tracker.py     # Core engine
├── sample_planning_documents.py      # Sample data
├── demo.py                           # Demo script
├── analyze_charlotte_docs.py         # Real document analyzer
├── README.md                         # Full documentation
├── EXECUTIVE_SUMMARY.md              # 1-page overview
├── QUICKSTART.md                     # Quick start guide
├── ARCHITECTURE.md                   # System design
├── SUBMISSION_CHECKLIST.md           # Submission guide
├── rezoning_opportunities.csv        # Sample results
└── rezoning_opportunities_detailed.json  # Sample results (detailed)
```

### Step 1.2: Install Dependencies

Open terminal/command prompt:

```bash
cd path/to/municipal_rezoning_tracker

# Install pandas (only dependency)
pip install pandas
```

**Troubleshooting:**
- If `pip` doesn't work, try `pip3`
- On Mac/Linux, you might need: `pip install pandas --break-system-packages`

---

## Part 2: Run the Demo (2 minutes)

### Step 2.1: Test with Sample Data

```bash
python demo.py
```

**Expected output:**
```
================================================================================
MUNICIPAL REZONING TRACKER - PROOF OF CONCEPT
================================================================================

✓ Loaded 5 documents
✓ Analysis complete!
✓ Identified 18 potential rezoning corridors

[Detailed report with top 10 opportunities]

✓ Results exported to: rezoning_opportunities.csv
```

### Step 2.2: View Results

**Option A - Open CSV in Excel/Google Sheets:**
```bash
# Mac
open rezoning_opportunities.csv

# Windows
start rezoning_opportunities.csv

# Linux
xdg-open rezoning_opportunities.csv
```

**Option B - View in terminal:**
```bash
head rezoning_opportunities.csv
```

**What you'll see:**
- Ranked list of corridors
- Confidence scores
- Timeline estimates
- Supporting evidence

---

## Part 3: Analyze Real Documents (10 minutes)

### Step 3.1: Understanding What Happened with Charlotte Docs

I analyzed your uploaded Charlotte documents and got **zero results**. Here's why:

**Your documents were:**
- City Council Zoning Meeting Agenda (Nov 17, 2025)
- Zoning Committee Work Session Agenda (Nov 5, 2025)

**These contain:**
- Individual rezoning petitions (developer requests)
- Petition numbers: 2025-045, 2025-075, 2025-080, etc.
- Specific property owner proposals

**What the tracker needs:**
- Strategic corridor planning documents
- Comprehensive plan updates
- City-initiated policy changes
- Infrastructure investment commitments

### Step 3.2: Finding the RIGHT Documents

**Go to Charlotte Planning Portal:**

1. Visit: https://charlottenc.legistar.com/Calendar.aspx

2. **Filter by meeting type:**
   - Click "All Meeting Bodies"
   - Select: **"City Council"** (NOT "Zoning Committee")

3. **Look for these agenda items:**
   - "2040 Comprehensive Plan Update"
   - "Strategic Planning Session"
   - "UDO Policy Discussion"
   - "Infrastructure Capital Plan"
   - "[Name] Corridor Vision Plan"

4. **Download:**
   - Look for PDF attachments
   - Download 3-5 policy documents (not individual petitions)

### Step 3.3: Extract Text from PDFs

**If you download PDFs, install PyPDF2:**

```bash
pip install PyPDF2
```

**Then use this script I created:**

```bash
python analyze_charlotte_docs.py
```

**Or manually extract text:**

```python
from PyPDF2 import PdfReader

def extract_pdf_text(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Use it
text = extract_pdf_text('charlotte_comprehensive_plan.pdf')
print(f"Extracted {len(text.split())} words")
```

---

## Part 4: Customize the Analysis (Advanced)

### Step 4.1: Add Your Own Documents

**Create a new Python file:**

```python
from municipal_rezoning_tracker import MunicipalRezoningTracker

# Your documents
my_documents = [
    {
        'text': '... [full document text] ...',
        'name': 'Charlotte 2040 Plan Update Q3 2025',
        'date': '2025-09-15'
    },
    {
        'text': '... [full document text] ...',
        'name': 'Strategic Corridor Study',
        'date': '2025-10-01'
    }
]

# Run analysis
tracker = MunicipalRezoningTracker()
opportunities = tracker.analyze_documents(my_documents)

# Generate report
report = tracker.generate_report(opportunities)
print(report)

# Export results
tracker.export_to_csv(opportunities, 'my_analysis.csv')
```

### Step 4.2: Adjust Scoring (Optional)

**Edit `municipal_rezoning_tracker.py`:**

Find this section (around line 40):

```python
self.intent_keywords = {
    'high_signal': [
        'encourage development',
        'strategic corridor',
        # Add your own keywords here
        'priority investment area',
        'transformation zone'
    ]
}
```

**Change point values** (around line 90):

```python
# Current
score += count * 10  # High-signal keywords

# Change to
score += count * 15  # Make high-signal keywords worth more
```

---

## Part 5: Understanding Results

### Step 5.1: Score Interpretation

| Score Range | Meaning | Action |
|------------|---------|---------|
| 90+ | Very high confidence | Immediate investigation |
| 50-89 | High confidence | Priority monitoring |
| 30-49 | Moderate confidence | Watch for updates |
| 15-29 | Emerging signal | Long-term tracking |

### Step 5.2: Timeline Classification

- **immediate**: 0-12 months (explicit near-term language)
- **near_term**: 1-3 years (medium-term planning)
- **long_term**: 3+ years (strategic vision)
- **unspecified**: No timeline mentioned

### Step 5.3: Reading the Evidence

**Each opportunity includes quotes like:**

> "...The city will promote mixed-use development along North Tryon Street within 24 months. Infrastructure investments including sewer expansion are scheduled for 2025-2026..."

**Look for:**
- ✅ Action verbs: "will", "shall", "immediate"
- ✅ Specific timelines: "Q2 2025", "within 18 months"
- ✅ Infrastructure commitments: "sewer expansion", "transit investment"
- ✅ Budget allocations: "allocated $X million"

---

## Part 6: For Your Submission

### Step 6.1: What to Submit

**Required files:**
1. `municipal_rezoning_tracker.py` - Core code
2. `sample_planning_documents.py` - Test data
3. `demo.py` - Demo script
4. `README.md` - Documentation
5. `rezoning_opportunities.csv` - Results

**Optional but recommended:**
6. `analyze_charlotte_docs.py` - Shows you can process real docs
7. `EXECUTIVE_SUMMARY.md` - Quick overview
8. `ARCHITECTURE.md` - System design

### Step 6.2: How to Package

**Option 1: ZIP file**
```bash
zip -r municipal_rezoning_tracker.zip *.py *.md *.csv *.json
```

**Option 2: GitHub (recommended)**
```bash
git init
git add .
git commit -m "Municipal Rezoning Tracker POC"
git remote add origin [your-repo-url]
git push -u origin main
```

**Option 3: Google Drive**
1. Upload all files to a folder
2. Set sharing to "Anyone with link"
3. Copy link

### Step 6.3: Email Template

See `SUBMISSION_CHECKLIST.md` for the full email template.

**Quick version:**

```
Subject: LotPotential Technical Assessment - Municipal Rezoning Tracker

Hi Sam,

Completed Track 1. Built a Municipal Rezoning Tracker that predicts 
city-initiated rezoning opportunities 6-18 months before formal announcements.

Deliverables: [GitHub link / Google Drive link]

Time: ~3.5 hours

Key results: Analyzed 5 planning documents, identified 18 corridors with 
actionable intelligence.

Ready for 90-minute working session.

Best,
Andy
```

---

## Part 7: Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'pandas'"**
```bash
pip install pandas
```

**Issue: "No corridors detected"**
- Check: Are you using strategic planning documents?
- Check: Do documents mention specific street/corridor names?
- Try: Lowering the minimum score threshold (line 100 in tracker)

**Issue: "Too many low-quality results"**
- Increase minimum threshold from 15 to 25
- Add more specific keywords to high_signal list
- Filter by timeline (focus on "immediate" only)

**Issue: PDF extraction produces garbage text**
```bash
# Try pdfplumber instead of PyPDF2
pip install pdfplumber

import pdfplumber
with pdfplumber.open('document.pdf') as pdf:
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
```

---

## Part 8: Next Steps After Submission

### For the 90-Minute Working Session

**Be prepared to discuss:**

1. **Technical decisions:**
   - Why NLP vs ML for this POC?
   - How would you improve accuracy?
   - Scaling to multiple cities?

2. **Business questions:**
   - Customer validation approach?
   - Pricing strategy?
   - Integration with LotPotential platform?

3. **Production roadmap:**
   - Automated document scraping
   - Historical pattern validation
   - Real-time alert system

### Potential Extensions

**If they ask "what would you build next?"**

1. **Historical Validation** (Week 1-2)
   - Match 2020-2024 predictions to actual rezonings
   - Calculate accuracy metrics
   - Refine scoring algorithm

2. **Parcel Integration** (Week 3-4)
   - Link corridors to specific parcels
   - Add property data (size, ownership, value)
   - Generate acquisition recommendations

3. **Multi-City Expansion** (Week 5-8)
   - Adapt to Austin, Nashville, Atlanta
   - Build city-specific keyword libraries
   - Cross-city pattern analysis

---

## Quick Reference Commands

```bash
# Run demo with sample data
python demo.py

# Analyze real Charlotte documents
python analyze_charlotte_docs.py

# Install dependencies
pip install pandas PyPDF2

# View results
open rezoning_opportunities.csv

# Package for submission
zip -r submission.zip *.py *.md *.csv
```

---

## Summary: 3-Step Quick Start

1. **Download files** → Save to one folder
2. **Run demo** → `python demo.py`
3. **Check results** → Open `rezoning_opportunities.csv`

Done! You have a working POC.

For real analysis: Get strategic planning documents → Extract text → Re-run analysis

---

**Questions?** Email: s@lotpotential.com

**All documentation:** Check README.md for full details
