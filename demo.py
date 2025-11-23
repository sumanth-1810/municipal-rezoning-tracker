"""
Demo Script: Municipal Rezoning Tracker
---------------------------------------
Demonstrates the complete analysis pipeline
"""

from municipal_rezoning_tracker import MunicipalRezoningTracker
from sample_planning_documents import get_sample_documents
import json

def main():
    print("\n" + "=" * 80)
    print("MUNICIPAL REZONING TRACKER - PROOF OF CONCEPT")
    print("=" * 80)
    print("\nInitializing tracker...")
    
    # Initialize the tracker
    tracker = MunicipalRezoningTracker()
    
    # Load sample documents
    print("Loading planning documents...")
    documents = get_sample_documents()
    print(f"✓ Loaded {len(documents)} documents\n")
    
    # Show what we're analyzing
    print("Documents being analyzed:")
    for i, doc in enumerate(documents, 1):
        word_count = len(doc['text'].split())
        print(f"  {i}. {doc['name']}")
        print(f"     Date: {doc['date']} | Words: {word_count:,}")
    
    print("\n" + "-" * 80)
    print("RUNNING ANALYSIS...")
    print("-" * 80 + "\n")
    
    # Run the analysis
    opportunities = tracker.analyze_documents(documents)
    
    print(f"✓ Analysis complete!")
    print(f"✓ Identified {len(opportunities)} potential rezoning corridors\n")
    
    # Generate and display report
    report = tracker.generate_report(opportunities, top_n=10)
    print(report)
    
    # Export to CSV
    csv_filename = 'rezoning_opportunities.csv'
    df = tracker.export_to_csv(opportunities, csv_filename)
    print(f"\n✓ Results exported to: {csv_filename}")
    print(f"✓ Total opportunities ranked: {len(df)}")
    
    # Generate summary statistics
    print("\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    
    # Timeline distribution
    timeline_dist = df['Timeline'].value_counts()
    print("\nTimeline Distribution:")
    for timeline, count in timeline_dist.items():
        print(f"  {timeline}: {count} corridors")
    
    # Top 5 opportunities
    print("\nTop 5 High-Probability Rezoning Opportunities:")
    print("-" * 80)
    for i, row in df.head(5).iterrows():
        print(f"\n{i+1}. {row['Corridor/Area']}")
        print(f"   Score: {row['Total Score']:.0f} | Timeline: {row['Timeline']}")
        print(f"   Mentioned in: {row['Documents']}")
    
    # Export detailed JSON for further analysis
    json_filename = 'rezoning_opportunities_detailed.json'
    with open(json_filename, 'w') as f:
        json.dump(opportunities, f, indent=2)
    print(f"\n✓ Detailed analysis exported to: {json_filename}")
    
    print("\n" + "=" * 80)
    print("KEY INSIGHTS")
    print("=" * 80)
    
    # Generate insights
    immediate_timeline = len(df[df['Timeline'] == 'immediate'])
    near_term = len(df[df['Timeline'] == 'near_term'])
    high_score = len(df[df['Total Score'] >= 50])
    
    print(f"""
1. IMMEDIATE OPPORTUNITIES: {immediate_timeline} corridors with explicit near-term timelines
   → These represent the highest-priority areas for developer focus

2. NEAR-TERM PIPELINE: {near_term} corridors with 1-3 year development windows
   → Strategic land acquisition targets before broader market recognition

3. HIGH-CONFIDENCE SIGNALS: {high_score} corridors with scores ≥50
   → Multiple document mentions + strong policy language + infrastructure investment

4. LEADING INDICATORS:
   • Infrastructure investment commitments (sewer, water, roads)
   • Specific timeline mentions in city documents
   • Use of action-oriented language ("will", "immediate", "priority")
   • Alignment with comprehensive plan goals

5. COMPETITIVE ADVANTAGE:
   • Municipal-initiated rezonings are announced 6-18 months before formal petitions
   • This tracker identifies opportunities BEFORE most developers are aware
   • Early positioning enables land acquisition at lower cost basis
    """)
    
    print("\n" + "=" * 80)
    print("PROOF OF CONCEPT COMPLETE")
    print("=" * 80)
    print("\nNext Steps for Production System:")
    print("  1. Automate document collection from Charlotte's planning portal")
    print("  2. Add historical pattern matching (compare to past successful rezonings)")
    print("  3. Integrate parcel-level data to identify specific investment opportunities")
    print("  4. Build alert system for new document releases")
    print("  5. Add competitive intelligence (track which developers are active in each corridor)")
    print("\n")


if __name__ == "__main__":
    main()
