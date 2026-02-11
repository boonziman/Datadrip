import feedparser  # For pulling RSS
import requests  # For API calls
import json  # For cache
import os  # For file handling
import re  # For sanitizing filenames
from datetime import datetime  # For dates
from secrets import HF_TOKEN, PEXELS_KEY  # Your keys

# Cache file for "learning" (stores past topics to avoid repeats and refine)
CACHE_FILE = 'cache.json'
if not os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'w') as f:
        json.dump({'past_topics': []}, f)

# Load cache
with open(CACHE_FILE, 'r') as f:
    cache = json.load(f)

# RSS feeds by category
feeds = {
    'ai': [
        'https://techcrunch.com/tag/artificial-intelligence/feed/',
        'http://news.mit.edu/rss/topic/artificial-intelligence2',
        'https://openai.com/blog/rss/',
        'https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml',
        'https://feeds.feedburner.com/blogspot/gJZg'
    ],
    'crypto': [
        'https://www.coindesk.com/arc/outboundfeeds/rss/',
        'https://cointelegraph.com/rss',
        'https://cryptoslate.com/feed/',
        'https://news.bitcoin.com/feed/',
        'https://cryptopotato.com/feed/'
    ],
    'tech': [
        'https://www.theverge.com/tech/rss/index.xml',
        'https://www.wired.com/feed/rss',
        'https://techcrunch.com/feed/',
        'https://www.technologyreview.com/feed/',
        'https://gizmodo.com/rss'
    ]
}

# Function to sanitize filename
def sanitize_filename(title):
    # Remove special characters and limit length
    title = re.sub(r'[^\w\s-]', '', title.lower())
    title = re.sub(r'[-\s]+', '-', title)
    return title[:60]  # Limit to 60 chars

# Function to generate content with AI (using Hugging Face Hub directly)
def generate_with_ai(prompt):
    try:
        from huggingface_hub import InferenceClient
        
        # Use Inference Client with a model that actually supports text generation
        client = InferenceClient(token=HF_TOKEN)
        
        # Try multiple models until one works
        models_to_try = [
            "mistralai/Mixtral-8x7B-Instruct-v0.1",  # Larger Mistral model
            "HuggingFaceH4/zephyr-7b-beta",  # Zephyr model
            "tiiuae/falcon-7b-instruct",  # Falcon model
        ]
        
        for model in models_to_try:
            try:
                response = client.text_generation(
                    prompt,
                    model=model,
                    max_new_tokens=2000,
                    temperature=0.7,
                    return_full_text=False
                )
                
                if response and len(response) > 500:
                    print(f"✓ AI generated {len(response)} characters using {model}")
                    return response
            except Exception as model_error:
                print(f"Model {model} failed: {str(model_error)[:100]}")
                continue
        
        # If all models fail, use fallback
        print("All AI models failed, using enhanced fallback")
        return create_fallback_content(prompt)
        
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return create_fallback_content(prompt)

# Fallback function to create high-quality content when AI API fails
def create_fallback_content(prompt):
    """Create a comprehensive blog post when AI API is unavailable"""
    lines = prompt.split('\n')
    title = "Breaking News"
    content_snippet = ""
    category_hint = ""
    
    # Extract title, content, and category from prompt
    for line in lines:
        if 'Title:' in line:
            title = line.split('Title:')[1].split('.')[0].strip()
        if 'Content:' in line:
            content_snippet = line.split('Content:')[1][:800].strip()
        if 'latest' in line and 'news' in line:
            if 'ai' in line.lower():
                category_hint = "AI"
            elif 'crypto' in line.lower():
                category_hint = "crypto"
            elif 'tech' in line.lower():
                category_hint = "tech"
    
    # Clean up HTML tags from content snippet
    import re
    content_snippet = re.sub(r'<[^>]+>', '', content_snippet)
    content_snippet = re.sub(r'&nbsp;', ' ', content_snippet)
    
    # Create structured, professional blog post with more substance
    return f"""## {title}: What You Need to Know in 2026

### Breaking Development in {category_hint if category_hint else 'Technology'}

{content_snippet}

This latest development in the {category_hint.lower() if category_hint else 'technology'} sector marks a significant shift in how the industry is evolving. As we dive deeper into 2026, these changes are reshaping the competitive landscape and creating new opportunities for innovation.

## In-Depth Analysis

### What's Really Happening

Industry experts are closely examining the implications of this announcement. The timing is particularly noteworthy given recent market trends and regulatory developments. This move could signal a broader transformation in how companies approach {category_hint.lower() if category_hint else 'technology'} challenges.

The technical aspects of this development deserve careful attention. According to industry analysts, the underlying technology represents a meaningful advancement over previous approaches. This isn't just incremental improvement—it's a fundamental rethinking of the problem space.

### Market Dynamics and Competitive Landscape

The competitive implications are substantial. Major players in the {category_hint.lower() if category_hint else 'tech'} industry are likely reassessing their strategies in light of this news. We're already seeing early indicators of market repositioning:

- **Investment Flows**: Venture capital and strategic investors are adjusting their focus areas
- **Talent Competition**: Companies are ramping up hiring in related specializations  
- **Partnership Strategies**: New alliances are forming to capitalize on emerging opportunities
- **Technology Roadmaps**: Development priorities are being recalibrated across the sector

### Key Implications for 2026 and Beyond

The announcement has catalyzed significant discussion among industry professionals, investors, and analysts. Here's what stakeholders need to understand:

**For Investors:** This development could influence portfolio strategies and sector allocations. The risk/reward profile of related investments may be shifting, requiring careful evaluation of exposure and timing.

**For Enterprises:** Organizations need to consider how this affects their technology roadmaps, competitive positioning, and strategic partnerships. Early movers may gain advantage, but prudent assessment is essential.

**For Developers and Technical Professionals:** New skill requirements and career opportunities are emerging. Staying current with these developments is crucial for professional growth.

**For Consumers and End Users:** The ultimate impact will be felt in product experiences, pricing dynamics, and service availability. Understanding these changes helps in making informed decisions.

## Industry Expert Perspectives

Leading analysts in the {category_hint.lower() if category_hint else 'technology'} space are offering varied interpretations. While some view this as a watershed moment, others counsel measured expectations. The consensus emerging from expert commentary suggests:

1. **Short-term volatility** is likely as markets digest and respond to the news
2. **Long-term structural changes** are probable, though the exact trajectory remains uncertain  
3. **Technology adoption patterns** will be critical to watch in coming quarters
4. **Regulatory considerations** may play a larger role than initially apparent
5. **International implications** extend beyond immediate geographic markets

## What to Watch Moving Forward

### Critical Indicators

As this situation evolves, several key metrics and developments will provide important signals:

**Technical Milestones:** Implementation progress, performance benchmarks, and scalability demonstrations will validate or challenge initial promises.

**Market Response:** User adoption rates, revenue impacts, and market share shifts will reveal real-world reception.

**Competitive Reactions:** How rivals respond—through their own innovations, partnerships, or strategic pivots—will shape the competitive landscape.

**Regulatory Developments:** Government and regulatory body actions could significantly influence outcomes.

### Timeline Expectations

Industry observers are mapping out likely progression:

- **Next 30 days:** Initial market reactions and competitor responses
- **Q1-Q2 2026:** Early adoption data and performance metrics  
- **Second half 2026:** Broader market impact becomes clearer
- **2027 outlook:** Long-term trajectory and sustainability assessment

## Strategic Implications

### For Decision Makers

Leaders across the {category_hint.lower() if category_hint else 'technology'} ecosystem should consider:

**Scenario Planning:** Develop strategies for multiple potential outcomes. The situation remains fluid, and agility will be valuable.

**Capability Building:** Assess whether internal capabilities align with emerging requirements. Strategic investments in talent, technology, or partnerships may be warranted.

**Stakeholder Communication:** Clear, proactive communication with investors, employees, customers, and partners will be essential as the situation develops.

### Risk and Opportunity Assessment

Every significant market shift creates both risks and opportunities. The current development is no exception:

**Upside Potential:** Organizations that position effectively could capture significant value through market share gains, pricing power, or strategic optionality.

**Downside Risks:** Those slow to adapt or poorly positioned may face competitive disadvantages, stranded investments, or strategic misalignment.

## The Broader Context

This news doesn't exist in isolation. It's part of larger trends reshaping the {category_hint.lower() if category_hint else 'technology'} industry in 2026:

- **Digital Transformation Acceleration:** Organizations across sectors are deepening their technology integration
- **Emerging Technology Convergence:** AI, blockchain, cloud, and other technologies are combining in powerful new ways
- **Changing Regulatory Landscape:** Governments worldwide are updating frameworks to address new realities  
- **Shifting Investment Patterns:** Capital is flowing toward areas with compelling long-term potential
- **Evolving User Expectations:** Customers are demanding more sophisticated, integrated, and personalized experiences

## Conclusion: Navigating Uncertainty

As we continue tracking this developing story, maintaining perspective is important. While the immediate headlines grab attention, the lasting impact will unfold over time. Success will come to those who:

1. **Stay informed** about ongoing developments  
2. **Think strategically** about implications for their specific context
3. **Act decisively** when opportunities align with capabilities
4. **Remain flexible** as new information emerges

The {category_hint.lower() if category_hint else 'technology'} industry in 2026 is dynamic, complex, and full of potential. This latest development adds another important chapter to an ongoing story of transformation and innovation.

---

*DataDrip is committed to providing timely, insightful analysis of developments in AI, cryptocurrency, and technology. Follow us for continued coverage of this story and other breaking news shaping the digital landscape.*

**Have thoughts on this development? We'd love to hear your perspective on how this might impact your industry or organization.**
"""

# Main loop: Generate 1-2 posts per category
for category, feed_list in feeds.items():
    posts_generated = 0
    for feed_url in feed_list:
        if posts_generated >= 2:  # Limit to 2 per category for testing/daily
            break
            
        try:
            feed = feedparser.parse(feed_url)
            if not feed.entries:
                continue
                
            for entry in feed.entries[:1]:  # Take latest entry
                if posts_generated >= 2:
                    break
                    
                title = entry.title
                content = ""
                
                # Get content from various possible fields
                if hasattr(entry, 'content'):
                    content = entry.content[0].value
                elif hasattr(entry, 'description'):
                    content = entry.description
                elif hasattr(entry, 'summary'):
                    content = entry.summary
                
                # Avoid repeats using cache
                if any(title.lower() in past.lower() for past in cache['past_topics']):
                    print(f"Skipping duplicate: {title}")
                    continue
                
                # Smart prompt for original, SEO-optimized post
                prompt = f"""Write a comprehensive, professional blog post based on this breaking news:

Title: {title}
Content Summary: {content[:1200]}
Category: {category.upper()}

Your Task: Create an original 1000-1500 word blog post for DataDrip, a professional tech news site.

Structure (REQUIRED):
1. **Compelling Headline** (SEO-optimized, include '2026', '{category}', 'news')
2. **Executive Summary** (2-3 paragraphs): What happened, why it matters now
3. **Deep Dive Analysis** (4-5 paragraphs): 
   - Technical details and context
   - Industry implications
   - Expert perspective and unique insights
4. **Key Takeaways** (5-7 bullet points): Actionable insights
5. **Market Impact** (2-3 paragraphs): How this affects stakeholders, investors, users
6. **Looking Forward** (2 paragraphs): Predictions, what to watch
7. **Conclusion** (1 paragraph): Summary and call-to-action

Tone: Professional yet accessible, authoritative, insightful
Style: Like TechCrunch or The Verge - engaging but informative
SEO: Naturally include keywords: {category}, 2026, technology, innovation, industry

IMPORTANT: 
- Write in original language, NOT copied from source
- Include specific details, data points, and analysis
- Add your own insights and perspective
- Make it compelling and worth reading
- Use markdown formatting (##, ###, bold, lists)

Write the complete blog post now:"""
                
                print(f"Generating content for: {title}")
                generated_content = generate_with_ai(prompt)
                
                if not generated_content or len(generated_content) < 200:
                    print(f"Using fallback content for: {title}")
                    generated_content = create_fallback_content(prompt)
                
                # Extract title from generated content or use original title
                new_title = title  # Use the actual RSS feed title by default
                
                # Only try to extract from generated if it's AI content
                if "# " in generated_content[:200]:
                    lines = generated_content.split('\n')
                    for line in lines[:5]:
                        if line.strip().startswith('#') and len(line.strip()) > 3:
                            potential_title = line.replace('#', '').strip()
                            # Only use if it's not the generic prompt title
                            if 'seo-optimized' not in potential_title.lower():
                                new_title = potential_title
                            break
                
                meta_desc = f"Latest {category} insights on DataDrip: {new_title[:100]}"
                
                # Fetch image from Pexels
                image_url = ''
                alt_text = f"{category} news image"
                try:
                    search_query = new_title.replace(' ', '%20')
                    pexels_url = f"https://api.pexels.com/v1/search?query={search_query}&per_page=1"
                    headers = {"Authorization": PEXELS_KEY}
                    response = requests.get(pexels_url, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('photos') and len(data['photos']) > 0:
                            image_url = data['photos'][0]['src']['large']
                            alt_text = data['photos'][0].get('alt') or alt_text
                except Exception as e:
                    print(f"Error fetching image: {e}")
                
                # Save as Markdown in _posts/
                date_str = datetime.now().strftime('%Y-%m-%d')
                safe_title = sanitize_filename(new_title)
                filename = f"_posts/{date_str}-{safe_title}.md"
                
                # Ensure _posts directory exists
                os.makedirs('_posts', exist_ok=True)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"""---
layout: post
title: "{new_title}"
date: {date_str}
categories: [ {category} ]
description: "{meta_desc}"
image: {image_url if image_url else 'assets/images/logo.png'}
author: sal
---

{generated_content}

""")
                    
                    # Add image if available
                    if image_url:
                        f.write(f"\n![{alt_text}]({image_url})\n")
                
                # Update cache
                cache['past_topics'].append(new_title)
                with open(CACHE_FILE, 'w') as f:
                    json.dump(cache, f, indent=2)
                
                print(f"✓ Generated post: {filename}")
                posts_generated += 1
                
        except Exception as e:
            print(f"Error processing feed {feed_url}: {e}")
            continue

print(f"\n=== Content generation complete ===")
print(f"Total posts created: Check _posts/ directory")
