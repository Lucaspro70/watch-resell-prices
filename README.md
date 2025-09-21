# Watch Resell Price Tracker

A comprehensive tool to help track watch resell prices from Facebook Marketplace and retail sources to make informed buying and selling decisions for your watch reselling business.

## Features

🎯 **Multi-Source Price Tracking**
- Facebook Marketplace sold price analysis
- Retail price lookup and comparison
- Profit margin calculations
- Investment recommendations

📊 **Comprehensive Analysis**
- Average, minimum, and maximum sold prices
- Recent sales history with details
- Profit margin percentages
- Color-coded recommendations

💡 **Business Intelligence**
- Identifies profitable watch models
- Calculates buy/sell price points
- Historical data caching
- Interactive and batch modes

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lucaspro70/watch-resell-prices.git
cd watch-resell-prices
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Mode

Search for a specific watch model:
```bash
python watch_tracker.py "Rolex Submariner"
```

### Interactive Mode

Run in interactive mode to search multiple watches:
```bash
python watch_tracker.py --interactive
```

Or use the short flag:
```bash
python watch_tracker.py -i
```

### Example Output

```
⌚ Welcome to Watch Resell Price Tracker
==================================================

🔍 Searching for pricing data for: Rolex Submariner
💰 Retail Price: $8,100.00
📱 Searching Facebook Marketplace...
📊 Found 3 recent sales

============================================================
📊 WATCH PRICING SUMMARY
============================================================

🎯 Model: Rolex Submariner
💰 Retail Price: $8,100.00

📈 Recent Sales Analysis:
   Average Sold Price: $6,833.33
   Price Range: $6,500.00 - $7,200.00
   Profit Margin: -15.6%

🎯 Recommendation: AVOID - Potential loss or break-even

📝 Recent Sales Details:
   1. $6,800.00 - Used - Excellent - 2025-09-16 - New York, NY
   2. $6,500.00 - Used - Good - 2025-09-09 - Los Angeles, CA
   3. $7,200.00 - Used - Like New - 2025-09-03 - Miami, FL
```

## Recommendation System

The tool provides color-coded recommendations based on profit margins:

- 🟢 **EXCELLENT** (>30% margin): High profit potential
- 🟡 **GOOD** (15-30% margin): Decent profit margin
- 🟡 **FAIR** (5-15% margin): Low but positive margin
- 🔴 **AVOID** (<5% margin): Potential loss or break-even

## Data Sources

### Current Implementation
- **Retail Prices**: Built-in database with common watch models
- **Marketplace Data**: Sample data structure ready for integration

### Production Integration Points
The application is designed to integrate with:

1. **Facebook Marketplace**
   - Graph API (limited access)
   - Third-party aggregation services
   - Manual data entry tools

2. **Retail Price Sources**
   - Watch manufacturer websites
   - Authorized dealer APIs
   - Price comparison services

3. **Additional Marketplaces**
   - eBay sold listings
   - Chrono24 data
   - Local marketplace platforms

## Data Storage

- **Local Cache**: `watch_data.json` stores search results locally
- **Historical Tracking**: Timestamps and price history
- **Easy Export**: JSON format for data analysis

## Advanced Features

### Web Scraping Framework

The included `scraper.py` module provides a foundation for:
- eBay sold listings analysis
- Retail price lookups
- Marketplace data aggregation

```bash
python scraper.py  # Demo the scraping framework
```

### Extensibility

The modular design allows easy addition of:
- New data sources
- Custom recommendation algorithms
- Export formats (CSV, Excel, etc.)
- Database integration

## Technical Details

### Dependencies
- `requests`: HTTP client for API calls
- `beautifulsoup4`: Web scraping capabilities
- `pandas`: Data analysis and processing
- `click`: CLI interface
- `colorama`: Colored terminal output
- `python-dateutil`: Date/time handling

### Project Structure
```
watch-resell-prices/
├── watch_tracker.py    # Main application
├── scraper.py         # Web scraping framework
├── requirements.txt   # Dependencies
├── watch_data.json    # Cached data (auto-generated)
└── README.md         # Documentation
```

## Important Notes

### Legal and Ethical Considerations

- **Facebook Marketplace**: Direct scraping violates Terms of Service. Use official APIs where available.
- **Rate Limiting**: Always respect website rate limits and robots.txt
- **Data Usage**: Only use data for personal/business analysis, not redistribution

### Limitations

- **Sample Data**: Current implementation uses sample data for demonstration
- **API Access**: Production use requires proper API keys and permissions
- **Market Variations**: Prices vary by location, condition, and market timing

## Contributing

This tool is designed for personal use in watch reselling business. To extend functionality:

1. Add new retail price sources in `get_retail_price()`
2. Implement real marketplace APIs in the scraper module
3. Enhance recommendation algorithms
4. Add new output formats

## License

This project is for personal/business use. Please respect the Terms of Service of all data sources and marketplaces.

## Disclaimer

This tool is for educational and business planning purposes. Always verify prices and market conditions before making investment decisions. The authors are not responsible for any financial losses.
