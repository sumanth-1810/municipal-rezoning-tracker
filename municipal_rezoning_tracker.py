"""
Municipal Rezoning Tracker & Opportunity Mapper
------------------------------------------------
Analyzes planning documents to predict city-initiated rezoning opportunities

Technical Approach:
1. Text extraction from planning documents
2. NLP-based corridor/area identification
3. Policy language change detection
4. Temporal pattern analysis
5. Opportunity scoring and ranking
"""

import re
import pandas as pd
from collections import defaultdict, Counter
from datetime import datetime
import json

class MunicipalRezoningTracker:
    """
    Identifies high-probability municipal rezoning opportunities by analyzing
    comprehensive plan updates, UDO amendments, and policy documents.
    """
    
    def __init__(self):
        # Keywords that signal rezoning intent
        self.intent_keywords = {
            'high_signal': [
                'encourage development', 'promote mixed-use', 'transit-oriented',
                'strategic corridor', 'priority area', 'future growth',
                'redevelopment opportunity', 'transformation', 'master plan update'
            ],
            'medium_signal': [
                'consider rezoning', 'evaluate', 'study area', 'potential',
                'appropriate for', 'consistent with', 'align with'
            ],
            'infrastructure': [
                'sewer expansion', 'water infrastructure', 'transit investment',
                'road improvements', 'utility extension'
            ]
        }
        
        # Geographic patterns (can be expanded with actual Charlotte data)
        self.corridor_patterns = [
            r'(?:along|near|adjacent to|corridor)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+(?:Street|Road|Boulevard|Avenue|Drive|Parkway|Highway|Corridor)))',
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:corridor|area|district|neighborhood)',
            r'(?:between|from)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:and|to)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
        ]
        
        self.results = []
        
    def extract_corridors(self, text):
        """Extract geographic areas and corridors from text"""
        corridors = set()
        
        # Common words to filter out (not actual corridors)
        stop_words = {'the', 'this', 'these', 'those', 'that', 'a', 'an', 'and', 'or', 
                      'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from'}
        
        for pattern in self.corridor_patterns:
            matches = re.finditer(pattern, text)
            for match in matches:
                # Get all captured groups
                for group in match.groups():
                    if group:
                        corridor = group.strip()
                        # Filter out stop words and very short names
                        if (corridor.lower() not in stop_words and 
                            len(corridor) > 3 and
                            not corridor.lower() in ['area', 'corridor', 'district', 'street']):
                            corridors.add(corridor)
        
        return list(corridors)
    
    def calculate_signal_strength(self, text, corridor):
        """
        Calculate signal strength for a corridor based on surrounding context
        Returns score 0-100
        """
        # Create a window around corridor mentions
        corridor_contexts = []
        pattern = re.escape(corridor)
        
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start = max(0, match.start() - 300)
            end = min(len(text), match.end() + 300)
            corridor_contexts.append(text[start:end].lower())
        
        if not corridor_contexts:
            return 0
        
        score = 0
        context_text = ' '.join(corridor_contexts)
        
        # High signal keywords (10 points each)
        for keyword in self.intent_keywords['high_signal']:
            count = context_text.count(keyword.lower())
            score += count * 10
        
        # Medium signal keywords (5 points each)
        for keyword in self.intent_keywords['medium_signal']:
            count = context_text.count(keyword.lower())
            score += count * 5
        
        # Infrastructure mentions (bonus 8 points each)
        for keyword in self.intent_keywords['infrastructure']:
            count = context_text.count(keyword.lower())
            score += count * 8
        
        # Frequency bonus (more mentions = higher confidence)
        mention_count = len(corridor_contexts)
        score += min(mention_count * 3, 20)  # Cap at 20 points
        
        return min(score, 100)  # Cap at 100
    
    def extract_timeline_signals(self, text, corridor):
        """Extract timeline indicators from text"""
        corridor_contexts = []
        pattern = re.escape(corridor)
        
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start = max(0, match.start() - 200)
            end = min(len(text), match.end() + 200)
            corridor_contexts.append(text[start:end])
        
        context_text = ' '.join(corridor_contexts)
        
        # Look for timeline indicators
        timeline_patterns = {
            'immediate': [r'within (\d+) months?', r'by (\d{4})', r'next year', r'immediate'],
            'near_term': [r'within (\d+) years?', r'short[- ]term', r'upcoming'],
            'long_term': [r'long[- ]term', r'future', r'eventual', r'phase [2-9]']
        }
        
        timelines = []
        for category, patterns in timeline_patterns.items():
            for pattern in patterns:
                if re.search(pattern, context_text, re.IGNORECASE):
                    timelines.append(category)
                    break
        
        return timelines[0] if timelines else 'unspecified'
    
    def extract_supporting_evidence(self, text, corridor, max_quotes=3):
        """Extract relevant quotes mentioning the corridor"""
        evidence = []
        pattern = re.escape(corridor)
        
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start = max(0, match.start() - 150)
            end = min(len(text), match.end() + 150)
            
            quote = text[start:end].strip()
            # Clean up the quote
            quote = ' '.join(quote.split())
            if len(quote) > 50:  # Only keep substantial quotes
                evidence.append(f"...{quote}...")
                
            if len(evidence) >= max_quotes:
                break
        
        return evidence
    
    def analyze_document(self, document_text, document_name, document_date):
        """
        Analyze a single planning document
        Returns list of opportunities found
        """
        opportunities = []
        
        # Extract all corridors mentioned
        corridors = self.extract_corridors(document_text)
        
        for corridor in corridors:
            signal_strength = self.calculate_signal_strength(document_text, corridor)
            
            # Only include corridors with meaningful signal
            if signal_strength >= 15:
                timeline = self.extract_timeline_signals(document_text, corridor)
                evidence = self.extract_supporting_evidence(document_text, corridor, max_quotes=2)
                
                opportunity = {
                    'corridor': corridor,
                    'signal_strength': signal_strength,
                    'timeline': timeline,
                    'source_document': document_name,
                    'document_date': document_date,
                    'evidence': evidence
                }
                
                opportunities.append(opportunity)
        
        return opportunities
    
    def analyze_documents(self, documents):
        """
        Analyze multiple documents and aggregate results
        
        Args:
            documents: List of dicts with keys: 'text', 'name', 'date'
        """
        all_opportunities = []
        
        for doc in documents:
            opportunities = self.analyze_document(
                doc['text'], 
                doc['name'], 
                doc['date']
            )
            all_opportunities.extend(opportunities)
        
        # Aggregate by corridor (a corridor might appear in multiple documents)
        corridor_data = defaultdict(lambda: {
            'total_score': 0,
            'documents': [],
            'timelines': [],
            'evidence': []
        })
        
        for opp in all_opportunities:
            corridor = opp['corridor']
            corridor_data[corridor]['total_score'] += opp['signal_strength']
            corridor_data[corridor]['documents'].append({
                'name': opp['source_document'],
                'date': opp['document_date'],
                'score': opp['signal_strength']
            })
            corridor_data[corridor]['timelines'].append(opp['timeline'])
            corridor_data[corridor]['evidence'].extend(opp['evidence'])
        
        # Create final ranking
        ranked_opportunities = []
        for corridor, data in corridor_data.items():
            # Determine most urgent timeline
            timeline_priority = {'immediate': 1, 'near_term': 2, 'long_term': 3, 'unspecified': 4}
            best_timeline = min(data['timelines'], key=lambda x: timeline_priority.get(x, 4))
            
            ranked_opportunities.append({
                'corridor': corridor,
                'total_score': data['total_score'],
                'avg_score': data['total_score'] / len(data['documents']),
                'num_mentions': len(data['documents']),
                'timeline': best_timeline,
                'documents': data['documents'],
                'evidence': list(set(data['evidence']))[:3]  # Top 3 unique pieces of evidence
            })
        
        # Sort by total score
        ranked_opportunities.sort(key=lambda x: x['total_score'], reverse=True)
        
        return ranked_opportunities
    
    def generate_report(self, ranked_opportunities, top_n=10):
        """Generate a formatted report of top opportunities"""
        report = []
        report.append("=" * 80)
        report.append("MUNICIPAL REZONING OPPORTUNITY TRACKER - ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        for i, opp in enumerate(ranked_opportunities[:top_n], 1):
            report.append(f"\n#{i} - {opp['corridor']}")
            report.append("-" * 80)
            report.append(f"Overall Score: {opp['total_score']:.1f} | Timeline: {opp['timeline']}")
            report.append(f"Mentioned in {opp['num_mentions']} document(s)")
            report.append("")
            report.append("Source Documents:")
            for doc in opp['documents']:
                report.append(f"  • {doc['name']} ({doc['date']}) - Score: {doc['score']}")
            report.append("")
            report.append("Supporting Evidence:")
            for evidence in opp['evidence'][:2]:
                report.append(f"  • {evidence[:200]}...")
            report.append("")
        
        return "\n".join(report)
    
    def export_to_csv(self, ranked_opportunities, filename):
        """Export results to CSV for further analysis"""
        rows = []
        for opp in ranked_opportunities:
            rows.append({
                'Corridor/Area': opp['corridor'],
                'Total Score': opp['total_score'],
                'Average Score': round(opp['avg_score'], 1),
                'Mentions': opp['num_mentions'],
                'Timeline': opp['timeline'],
                'Documents': ', '.join([d['name'] for d in opp['documents']]),
                'Top Evidence': opp['evidence'][0] if opp['evidence'] else ''
            })
        
        df = pd.DataFrame(rows)
        df.to_csv(filename, index=False)
        return df


if __name__ == "__main__":
    print("Municipal Rezoning Tracker initialized successfully")
    print("Ready to analyze planning documents")
