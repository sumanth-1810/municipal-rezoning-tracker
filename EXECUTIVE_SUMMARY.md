# Municipal Rezoning Tracker - Executive Summary

## The Feature

**Automated intelligence engine that predicts city-initiated rezoning opportunities 6-18 months before formal announcements by analyzing municipal planning documents.**

---

## Why 10× More Valuable

**Customer Pain Point (from interviews):**
"Off-Market Land Discovery: Customers urgently need early access to potential land opportunities before they reach the public market."

**This Solution:**
- ✓ Identifies opportunities before broader market awareness
- ✓ Focuses on municipal-led rezonings (customer-identified "strong opportunity")
- ✓ Provides infrastructure investment signals (addresses utility visibility pain)
- ✓ Enables land acquisition at pre-market-awareness pricing (15-30% savings)

**Competitive Advantage:**
First-mover positioning on 6-18 month horizon opportunities that competitors won't discover until formal petitions.

---

## Technical Approach (3 Key Decisions)

### 1. NLP-Based Signal Detection
- Extract corridor mentions from planning documents
- Score based on policy language intensity ("encourage", "strategic", "immediate")
- Aggregate signals across multiple document types

### 2. Multi-Document Confidence Scoring
- Single mention = possible noise
- Multiple mentions + infrastructure investment = high confidence
- Evidence-based ranking with supporting quotes

### 3. Temporal Pattern Analysis  
- Extract timeline indicators ("within 18 months", "Q2 2025", "immediate")
- Prioritize opportunities with explicit near-term commitments
- Distinguish immediate vs long-term signals

---

## Business Case (One Paragraph)

This tracker solves the #1 customer pain point—off-market discovery—by providing 6-18 month lead time on municipal rezoning opportunities. Real estate developers would pay $750-1,500/month for this intelligence (comparable to existing tools like CoStar). With 20 customers, that's $30K MRR within 6 months. Early land acquisition at pre-announcement pricing delivers immediate ROI: saving 20% on a $2M land deal pays for 24 months of subscription. Expansion path: Charlotte → Top 10 Sunbelt metros → Historical pattern matching → Parcel-level recommendations.

---

## POC Results Summary

**Analysis:** 5 planning documents (1,300 words)  
**Output:** 18 ranked rezoning corridors with scores, timelines, and evidence

**Top 3 Opportunities:**
1. **North Tryon Street** (Score: 118) - TOD focus + sewer expansion commitment
2. **Independence Boulevard** (Score: 91) - BRT investment + TOD overlay expansion  
3. **Central Avenue** (Score: 62, Immediate timeline) - Vision plan refresh underway

**Key Insights Generated:**
- 8 corridors with immediate/near-term timelines (highest priority)
- Infrastructure investments (sewer, water, transit) correlate with rezoning signals
- Policy language analysis reveals certainty level ("will", "immediate", "priority")

---

## Time Invested

**~3.5 hours** (Requirements analysis, algorithm development, testing, documentation)

---

## Deliverables

✓ **Working Python code** (`municipal_rezoning_tracker.py`, `demo.py`)  
✓ **Sample data & analysis** (`sample_planning_documents.py`)  
✓ **Output files** (`rezoning_opportunities.csv`, detailed JSON)  
✓ **Technical documentation** (README.md with full implementation details)  
✓ **Business case** (above)

---

## Next Steps

**Production Development:**
1. Automate Charlotte document scraping (Legistar integration)
2. Historical validation against 2020-2024 actual rezonings
3. Add change detection & alert system
4. Parcel-level integration

**Customer Validation:**
1. Pilot with 2-3 developers
2. Validate: Does this change their land acquisition strategy?
3. Iterate based on feedback
4. Scale to additional metros

---

**Questions:** s@lotpotential.com  
**Ready for:** 90-minute working session
