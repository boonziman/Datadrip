# AI Content Generator Setup

## Step 1: Get API Keys

### Hugging Face Token
1. Go to https://huggingface.co/settings/tokens
2. Create a new token (read access is enough)
3. Copy the token

### Pexels API Key
1. Go to https://www.pexels.com/api/
2. Sign up for a free account
3. Get your API key from the dashboard

## Step 2: Configure secrets.py

Open `secrets.py` and replace the placeholder values:

```python
HF_TOKEN = "your_actual_huggingface_token_here"
PEXELS_KEY = "your_actual_pexels_api_key_here"
```

## Step 3: Run the Content Generator

Activate the virtual environment and run:

```bash
source .venv/bin/activate
python content_generator.py
```

## How It Works

1. **RSS Feeds**: Pulls latest articles from AI, crypto, and tech sources
2. **AI Generation**: Uses Mistral-7B via Hugging Face to create original content
3. **Images**: Fetches relevant images from Pexels API
4. **Caching**: Tracks past topics to avoid duplicates
5. **Jekyll Format**: Saves posts as markdown in `_posts/` with proper front matter

## Generated Post Structure

Each post includes:
- SEO-optimized title and meta description
- Proper category (ai, crypto, or tech)
- Featured image with alt text
- 800-1500 words of original content
- Professional structure (intro, analysis, takeaways)

## Automation (Optional)

To run daily automatically, set up a cron job or GitHub Action.

## Troubleshooting

- **API Rate Limits**: Free tiers have limits. Space out runs if needed.
- **Empty Content**: Check your API keys are valid
- **No Images**: Pexels might not have matching images; posts will use default logo
