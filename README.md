# Google Cloud Demo: Competitive Benchmarking Generator

An AI-powered business analysis tool that leverages Google's Gemini 2.5 Flash model to generate comprehensive competitive benchmarking reports for any company. The application provides strategic insights through automated SWOT analysis, key statistics, and actionable recommendations.

## What It Does

This application uses Google Cloud's Vertex AI and Gemini API to:

1. **Analyze any company** you specify
2. **Generate comprehensive business insights** including:
   - Company overview and key statistics
   - Complete SWOT analysis (Strengths, Weaknesses, Opportunities, Risks)
   - Strategic recommendations
   - Positive and negative implications of proposed strategies
3. **Export results** in multiple formats:
   - **PowerPoint (.pptx)** - Professional presentation slides
   - **CSV Table** - Structured data for analysis
   - **JSON** - Raw data for programmatic use

## Features

- 🤖 Powered by Google's Gemini 2.5 Flash AI model
- 📊 Multiple output formats (PowerPoint, CSV, JSON)
- 🎯 Comprehensive SWOT analysis
- 📈 Key business metrics and statistics
- 💡 Strategic recommendations with implications
- 🚀 Fast and automated report generation

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google Cloud Project with Vertex AI enabled
- Service account credentials with Vertex AI access

### Installation

1. **Clone the repository**
   ```bash
   cd google-cloud-demo
   ```

2. **Create a virtual environment**
   On macOS/Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```
   On Windows:
   ```bash
   python3 -m venv venv
   venv/scripts/activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install google-genai python-pptx python-dotenv pandas
   ```

4. **Configure environment variables**

   Create a `.env` file in the `google-cloud-demo` directory:
   ```bash
   PROJECT_ID=your-google-cloud-project-id
   GOOGLE_APPLICATION_CREDENTIALS=./credentials/service_account.json
   ```

5. **Add your service account key**

   Place your Google Cloud service account JSON key in:
   ```
   google-cloud-demo/credentials/service_account.json
   ```

## Usage

1. **Activate the virtual environment**
   On macOS/Linux:
   ```bash
   source venv/bin/activate  # MacOS/Linux
   ```
   On Windows:
   ```bash
   venv/scripts/activate  # Windows
   ```

2. **Run the application**
   ```bash
   python -m src.wrapper
   ```

3. **Follow the prompts**
   - Enter a company name (e.g., "Apple", "Tesla", "Google")
   - Choose output format:
     - `1` for PowerPoint
     - `2` for CSV Table
     - `3` for JSON

4. **Find your reports**
   - PowerPoint files: `powerpoints/`
   - CSV files: `tables/`
   - JSON files: `json_output/`

## Output Examples

### PowerPoint Output
Professional presentation with 7-8 slides including:
- Title slide with report name and analyst persona
- Overview & Key Stats slide
- 4 SWOT Analysis slides (Strengths, Weaknesses, Opportunities, Risks)
- Strategic Recommendations slide
- Implications slide

### CSV Output
Structured table with columns:
- Section (slide title)
- Type (Overview, Stat, Point, Positive, Negative)
- Content (detailed information)

### JSON Output
Complete structured data in JSON format with all analysis details 

Example Response from the Prompt to Gemini-2.5-Flash:
```yaml
{
  "reportTitle": "Google Business Analysis (Alphabet Inc.)",
  "analystPersona": "Prepared by AI Business Analyst",
  "slides": [
    {
      "slide_title": "Overview & Key Stats",
      "content": {
        "overview": "Alphabet Inc. (Google) is a global technology conglomerate renowned for its dominance in internet search, online advertising, cloud computing, and AI research. Its vast ecosystem includes products like Android, YouTube, Chrome, Google Cloud, and Pixel devices, serving billions of users worldwide and shaping the digital landscape.",
        "key_stats": [
          { "metric": "Market Capitalization (Approx.)", "value": "~$2.0 Trillion" },
          { "metric": "Annual Revenue (FY2023 Approx.)", "value": "~$305 Billion" },
          { "metric": "Search Market Share (Global)", "value": ">90%" },
          { "metric": "Employee Count (Q4 2023)", "value": "~180,000" },
          { "metric": "Primary Revenue Source", "value": "Advertising (Google Search, YouTube Ads, Google Network)" }      
        ]
      }
    },
    {
      "slide_title": "SWOT Analysis: Strengths",
      "content": [
        {
          "point": "Market Dominance & Ecosystem",
          "details": "Unrivaled global market share in search (Google), mobile OS (Android), and video (YouTube), creating powerful network effects and user lock-in."
        },
        {
          "point": "Innovation & R&D Leadership",
          "details": "Significant investment in cutting-edge technologies like AI (DeepMind, Gemini), quantum computing, and autonomous vehicles (Waymo), fostering continuous product evolution."
        },
        {
          "point": "Robust Financial Position",
          "details": "High profitability, substantial cash reserves, and diverse revenue streams enable strategic investments, acquisitions, and weathering economic downturns."
        },
        {
          "point": "Talent Pool & Brand Recognition",
          "details": "Attracts top global talent and possesses one of the most recognized and trusted technology brands worldwide."
        }
      ]
    },
    {
      "slide_title": "SWOT Analysis: Weaknesses",
      "content": [
        {
          "point": "Over-reliance on Advertising Revenue",
          "details": "Despite diversification efforts, a significant majority of revenue is still derived from advertising, making the company susceptible to economic downturns and ad market shifts."      
        },
        {
          "point": "Intense Regulatory Scrutiny",
          "details": "Constant antitrust investigations, data privacy regulations (e.g., GDPR, DMA), and legal challenges globally, leading to substantial fines and potential business model changes."      
        },
        {
          "point": "Data Privacy & Trust Concerns",
          "details": "Ongoing public and regulatory concerns regarding data collection, usage, and privacy practices can erode user trust and impact brand perception."
        },
        {
          "point": "Product Graveyard & Execution Inconsistency",
          "details": "A history of launching promising products only to discontinue them (e.g., Google+, Stadia), leading to user frustration and skepticism about new ventures."
        }
      ]
    },
    {
      "slide_title": "SWOT Analysis: Opportunities",
      "content": [
        {
          "point": "AI Integration & Monetization",
          "details": "Leverage leadership in AI (Gemini, DeepMind) to enhance existing products, create new services, and develop AI-first business solutions across various industries."
        },
        {
          "point": "Google Cloud Expansion",
          "details": "Significant untapped potential in the enterprise cloud market; growing market share against AWS and Azure through specialized services, hybrid cloud, and AI capabilities."
        },
        {
          "point": "Hardware Ecosystem Growth",
          "details": "Further integrate and expand the Pixel, Nest, and Fitbit hardware lines to build a more cohesive and competitive ecosystem, capturing more user value."
        },
        {
          "point": "Emerging Markets & Digital Inclusion",
          "details": "Tap into the 'next billion users' in developing economies with tailored, affordable products and services, expanding global reach and user base."
        }
      ]
    },
    {
      "slide_title": "SWOT Analysis: Risks",
      "content": [
        {
          "point": "Intensified Competition",
          "details": "Growing threats from rivals in AI (Microsoft/OpenAI), cloud (AWS, Azure), advertising (Meta, Amazon, TikTok), and hardware (Apple, Samsung)." 
        },
        {
          "point": "Adverse Regulatory & Legislative Changes",
          "details": "Risk of new antitrust laws, forced divestitures, stricter data localization requirements, or significant changes to digital advertising practices impacting profitability."
        },
        {
          "point": "AI Ethics & Misinformation",
          "details": "Potential for biased AI outputs, spread of deepfakes, and societal misuse of AI, leading to reputational damage, public backlash, and calls for stringent regulation."
        },
        {
          "point": "Economic Downturn & Ad Spend Contraction",
          "details": "Global economic instability or recession could lead to reduced advertising budgets from businesses, directly impacting Google's core revenue."
        }
      ]
    },
    {
      "slide_title": "Strategic Recommendations",
      "content": [
        {
          "recommendation": "Accelerate AI-First Product Transformation",
          "action": "Deeply integrate Gemini across all core products (Search, Workspace, Cloud, Android), prioritize AI-native feature development, and aggressively market Google's AI leadership to consumers and enterprises."
        },
        {
          "recommendation": "Aggressively Grow Google Cloud Market Share",        
          "action": "Invest heavily in enterprise sales and specialized industry solutions. Focus on hybrid cloud capabilities, data analytics, and generative AI offerings to differentiate from competitors and drive profitable growth."
        },
        {
          "recommendation": "Diversify Revenue Streams Beyond Ads",
          "action": "Expand subscription offerings (e.g., YouTube Premium, Workspace), scale hardware sales profitably, and explore new monetization models for AI-powered services and premium features across the ecosystem."
        },
        {
          "recommendation": "Proactively Address Regulatory & Privacy Concerns",  
          "action": "Engage constructively with policymakers globally, lead industry best practices in privacy and responsible AI development, and enhance transparency in data handling to build trust and mitigate legal risks."
        }
      ]
    },
    {
      "slide_title": "Implications of Strategic Recommendations",
      "content": {
        "positive_implications": [       
          {
            "point": "Enhanced Competitive Advantage & Innovation",
            "details": "Solidifies Google's position as an AI and technology leader, attracting users and developers, and creating new market opportunities."       
          },
          {
            "point": "Increased Revenue Stability & Growth",
            "details": "Diversification reduces reliance on advertising, while cloud growth and new monetization models create more resilient and predictable financial performance."
          },
          {
            "point": "Improved Brand Reputation & Trust",
            "details": "Proactive stances on privacy, responsible AI, and regulatory engagement can rebuild public trust and reduce the impact of legal challenges."
          },
          {
            "point": "Stronger Ecosystem & User Lock-in",
            "details": "Integrated AI across products and a robust hardware ecosystem increase user engagement and loyalty."
          }
        ],
        "negative_implications_of_inaction": [
          {
            "point": "Erosion of Market Dominance",
            "details": "Competitors, particularly in AI and cloud, could significantly close the gap or even surpass Google, leading to market share loss in key segments."
          },
          {
            "point": "Persistent Regulatory Headwinds & Fines",
            "details": "Continued legal battles and larger fines would divert significant resources, constrain innovation, and potentially lead to forced structural changes."
          },
          {
            "point": "Stagnation of Growth & Investor Skepticism",
            "details": "Over-reliance on existing advertising models without sufficient diversification would lead to slower growth, reduced profitability, and decreased investor confidence."
          },
          {
            "point": "Loss of Talent & Innovation Edge",
            "details": "A perceived lack of strategic direction or a decline in market leadership could lead to top talent departing for more innovative or stable environments."
          }
        ]
      }
    }
  ]
}
```
