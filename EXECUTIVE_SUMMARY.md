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

### 1. NLP-Based Signal Detection Over Machine Learning for MVP
Text pattern matching extracts corridor mentions from planning documents, then scores them based on surrounding policy language intensity ("strategic corridor", "encourage development" = high signal; "consider", "evaluate" = medium signal). This approach delivers immediate value without requiring historical training data and provides transparent, explainable predictions that customers can validate against source documents. Machine learning would be Phase 2 after accumulating labeled data from actual rezoning outcomes.

### 2. Multi-Document Confidence Aggregation with Evidence Trails
Single corridor mentions could be noise; repeated mentions across multiple document types (comprehensive plans + UDO amendments + council minutes + infrastructure budgets) indicate genuine municipal commitment. Each opportunity includes direct quotes from source documents, enabling customers to verify predictions and make informed investment decisions. The scoring algorithm weights by document type, policy language strength, and infrastructure investment mentions to quantify confidence.

### 3. Timeline Extraction Using Temporal Pattern Recognition
Regex patterns extract timeline indicators ("within 18 months", "Q2 2025", "immediate action recommended") from context windows around corridor mentions. Opportunities are classified as immediate (0-12 months), near-term (1-3 years), or long-term (3+ years), enabling customers to prioritize land acquisition strategy. Immediate-timeline corridors with high scores represent the highest-value opportunities requiring urgent action before market awareness.

### 4. Infrastructure Investment as Confidence Multiplier
Municipal mentions of sewer expansion, water infrastructure upgrades, and transit investments receive bonus scoring because they indicate genuine commitment beyond policy discussion. Infrastructure budgets are harder to change than zoning policy, making them more reliable predictors. This addresses customers' secondary pain point around utility infrastructure visibility while strengthening rezoning predictions.

### 5. Scalable Architecture for Production Deployment
POC designed with production in mind: modular components (extraction → analysis → scoring → output), clean interfaces for document ingestion, standardized output formats (CSV/JSON) for integration with LotPotential's existing pipeline, and keyword dictionaries that can be city-specific. The system processes documents in ~1 second each, enabling real-time analysis when new planning documents are published. Next step is automated document collection via Charlotte's Legistar API and webhook-based change detection.

---

## Business Case (One Paragraph)

This Municipal Rezoning Tracker directly solves LotPotential customers' #1 pain point off-market land discovery by providing 6-18 month lead time on municipal rezoning opportunities before broader market awareness. Real estate developers interviewed cited urgent need for early signal access; this tracker delivers that through automated analysis of public planning documents that are systematically under-analyzed by the market. The customer ROI is immediate and substantial: early land acquisition at pre-announcement pricing typically saves 15-30% on land costs, meaning a single $2M land deal generates $300K-600K in value enough to pay for 20+ years of subscription. With a target price of $750-1,500/month (comparable to existing tools like CoStar at $500-2,000/month), reaching just 20 customers yields $30K MRR within 6 months. The feature differentiates LotPotential by focusing on municipal-led rezonings rather than developer petitions a "strong opportunity" identified in customer interviews that "unlocks entirely new development corridors for multiple players" simultaneously. Expansion path is clear: validate in Charlotte (Phase 1), scale to top 10 Sunbelt metros where growth is fastest (Phase 2), add historical pattern matching to predict approval probability (Phase 3), and integrate parcel-level recommendations for specific acquisition targets (Phase 4). The competitive moat strengthens over time through network effects more customers provide more validation data, improving prediction accuracy and creating switching costs as the tracker becomes embedded in daily workflow.

---

## Time Invested

**~3.5 hours** (Requirements analysis, algorithm development, testing, documentation)

---

