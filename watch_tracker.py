#!/usr/bin/env python3
"""
Watch Resell Price Tracker

A tool to help track watch resell prices from Facebook Marketplace and retail sources
to make informed buying and selling decisions for watch reselling business.
"""

import click
import requests
import json
import time
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from colorama import init, Fore, Style, Back
import os

# Initialize colorama for colored output
init()

@dataclass
class WatchPrice:
    """Data class to represent watch pricing information"""
    model: str
    source: str
    price: float
    currency: str
    date: str
    condition: str
    location: str
    is_sold: bool
    url: Optional[str] = None

@dataclass
class WatchSummary:
    """Summary of watch pricing data"""
    model: str
    retail_price: Optional[float]
    avg_sold_price: Optional[float]
    min_sold_price: Optional[float] 
    max_sold_price: Optional[float]
    recent_sales: List[WatchPrice]
    profit_margin: Optional[float]
    recommendation: str
    suggested_buy_price: Optional[float] = None
    suggested_sell_price: Optional[float] = None

class WatchPriceTracker:
    """Main class for tracking watch prices"""
    
    def __init__(self):
        self.data_file = "watch_data.json"
        self.config_file = "config.json"
        self.load_config()
        self.load_cached_data()
    
    def load_config(self):
        """Load configuration settings"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                # Default configuration
                self.config = {
                    "recommendations": {
                        "excellent_margin": 30.0,
                        "good_margin": 15.0,
                        "fair_margin": 5.0
                    },
                    "display": {
                        "max_recent_sales": 10,
                        "use_colors": True
                    }
                }
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = {"recommendations": {"excellent_margin": 30.0, "good_margin": 15.0, "fair_margin": 5.0}}
    
    def load_cached_data(self):
        """Load cached price data from file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.cached_data = json.load(f)
            else:
                self.cached_data = {}
        except Exception as e:
            print(f"Error loading cached data: {e}")
            self.cached_data = {}
    
    def save_cached_data(self):
        """Save price data to cache file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.cached_data, f, indent=2)
        except Exception as e:
            print(f"Error saving cached data: {e}")
    
    def get_retail_price(self, watch_model: str) -> Optional[float]:
        """
        Get retail price for a watch model
        Note: This is a placeholder implementation that would connect to watch databases
        """
        # Sample retail prices for demonstration
        retail_prices = {
            "rolex submariner": 8100,
            "omega speedmaster": 5200,
            "tudor black bay": 3200,
            "seiko prospex": 250,
            "apple watch series 9": 399,
            "casio g-shock": 150,
            "tissot prc 200": 325,
            "citizen eco-drive": 200,
            "vintage omega": 800,  # Example of a good flip opportunity
            "vintage seiko": 100   # Another good flip opportunity
        }
        
        model_lower = watch_model.lower()
        for key, price in retail_prices.items():
            if key in model_lower:
                return price
        
        # If not found in sample data, return None (would implement API call here)
        return None
    
    def search_facebook_marketplace(self, watch_model: str) -> List[WatchPrice]:
        """
        Search Facebook Marketplace for watch prices
        Note: This is a placeholder implementation due to Facebook's API restrictions
        """
        # In a real implementation, this would require:
        # 1. Facebook Graph API access (limited for Marketplace)
        # 2. Web scraping (against ToS and technically challenging)
        # 3. Third-party APIs that aggregate marketplace data
        
        # For demonstration, return sample sold data
        sample_sales = [
            WatchPrice(
                model=watch_model,
                source="Facebook Marketplace",
                price=6800.0,
                currency="USD",
                date=(datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"),
                condition="Used - Excellent",
                location="New York, NY",
                is_sold=True,
                url="https://facebook.com/marketplace/item/..."
            ),
            WatchPrice(
                model=watch_model,
                source="Facebook Marketplace", 
                price=6500.0,
                currency="USD",
                date=(datetime.now() - timedelta(days=12)).strftime("%Y-%m-%d"),
                condition="Used - Good",
                location="Los Angeles, CA",
                is_sold=True,
                url="https://facebook.com/marketplace/item/..."
            ),
            WatchPrice(
                model=watch_model,
                source="Facebook Marketplace",
                price=7200.0,
                currency="USD", 
                date=(datetime.now() - timedelta(days=18)).strftime("%Y-%m-%d"),
                condition="Used - Like New",
                location="Miami, FL",
                is_sold=True,
                url="https://facebook.com/marketplace/item/..."
            )
        ]
        
        # Filter sample data based on watch model
        model_lower = watch_model.lower()
        if "rolex" in model_lower and "submariner" in model_lower:
            return sample_sales
        elif "vintage omega" in model_lower:
            # Good profit example - vintage watches often sell well
            adjusted_sales = []
            base_prices = [1200, 950, 1100]  # More realistic vintage Omega prices
            for i, sale in enumerate(sample_sales):
                new_sale = WatchPrice(
                    model=watch_model,
                    source="Facebook Marketplace",
                    price=base_prices[i],
                    currency="USD",
                    date=sale.date,
                    condition=sale.condition,
                    location=sale.location,
                    is_sold=True,
                    url=sale.url
                )
                adjusted_sales.append(new_sale)
            return adjusted_sales
        elif "vintage seiko" in model_lower:
            # Another good profit example
            adjusted_sales = []
            base_prices = [180, 150, 220]  # Good vintage Seiko prices
            for i, sale in enumerate(sample_sales):
                new_sale = WatchPrice(
                    model=watch_model,
                    source="Facebook Marketplace", 
                    price=base_prices[i],
                    currency="USD",
                    date=sale.date,
                    condition=sale.condition,
                    location=sale.location,
                    is_sold=True,
                    url=sale.url
                )
                adjusted_sales.append(new_sale)
            return adjusted_sales
        elif any(term in model_lower for term in ["omega", "speedmaster"]):
            # Adjust prices for Omega
            adjusted_sales = []
            for sale in sample_sales:
                new_sale = WatchPrice(
                    model=watch_model,
                    source=sale.source,
                    price=sale.price * 0.65,  # Omega typically lower than Rolex
                    currency=sale.currency,
                    date=sale.date,
                    condition=sale.condition,
                    location=sale.location,
                    is_sold=sale.is_sold,
                    url=sale.url
                )
                adjusted_sales.append(new_sale)
            return adjusted_sales
        elif any(term in model_lower for term in ["tudor", "black bay"]):
            adjusted_sales = []
            for sale in sample_sales:
                new_sale = WatchPrice(
                    model=watch_model,
                    source=sale.source,
                    price=sale.price * 0.4,
                    currency=sale.currency,
                    date=sale.date,
                    condition=sale.condition,
                    location=sale.location,
                    is_sold=sale.is_sold,
                    url=sale.url
                )
                adjusted_sales.append(new_sale)
            return adjusted_sales
        else:
            # Return empty for unknown models in demo
            return []
    
    def calculate_profit_analysis(self, retail_price: Optional[float], sold_prices: List[float]) -> Dict[str, Any]:
        """Calculate profit margins and recommendations"""
        if not sold_prices:
            return {
                "avg_sold_price": None,
                "profit_margin": None,
                "recommendation": "No recent sales data available"
            }
        
        avg_sold = sum(sold_prices) / len(sold_prices)
        min_sold = min(sold_prices)
        max_sold = max(sold_prices)
        
        analysis = {
            "avg_sold_price": avg_sold,
            "min_sold_price": min_sold,
            "max_sold_price": max_sold
        }
        
        if retail_price:
            profit_margin = ((avg_sold - retail_price) / retail_price) * 100
            analysis["profit_margin"] = profit_margin
            
            excellent_threshold = self.config["recommendations"]["excellent_margin"]
            good_threshold = self.config["recommendations"]["good_margin"]
            fair_threshold = self.config["recommendations"]["fair_margin"]
            
            if profit_margin > excellent_threshold:
                analysis["recommendation"] = "EXCELLENT - High profit potential"
            elif profit_margin > good_threshold:
                analysis["recommendation"] = "GOOD - Decent profit margin"
            elif profit_margin > fair_threshold:
                analysis["recommendation"] = "FAIR - Low but positive margin"
            else:
                analysis["recommendation"] = "AVOID - Potential loss or break-even"
            
            # Add suggested buy/sell prices
            analysis["suggested_buy_price"] = avg_sold * 0.8  # Buy at 80% of avg sold price
            analysis["suggested_sell_price"] = avg_sold * 0.95  # Sell at 95% of avg sold price
        else:
            analysis["profit_margin"] = None
            if avg_sold > 1000:
                analysis["recommendation"] = "RESEARCH NEEDED - High value item, verify retail price"
            else:
                analysis["recommendation"] = "RESEARCH NEEDED - Unknown retail price"
        
        return analysis
    
    def track_watch(self, watch_model: str) -> WatchSummary:
        """Main method to track a watch and return comprehensive pricing data"""
        print(f"\n🔍 Searching for pricing data for: {Fore.CYAN}{watch_model}{Style.RESET_ALL}")
        
        # Get retail price
        retail_price = self.get_retail_price(watch_model)
        if retail_price:
            print(f"💰 Retail Price: {Fore.GREEN}${retail_price:,.2f}{Style.RESET_ALL}")
        else:
            print(f"💰 Retail Price: {Fore.YELLOW}Not found{Style.RESET_ALL}")
        
        # Get Facebook Marketplace data
        print("📱 Searching Facebook Marketplace...")
        fb_sales = self.search_facebook_marketplace(watch_model)
        
        if fb_sales:
            print(f"📊 Found {len(fb_sales)} recent sales")
        else:
            print(f"{Fore.YELLOW}⚠️  No recent sales found{Style.RESET_ALL}")
        
        # Calculate profit analysis
        sold_prices = [sale.price for sale in fb_sales if sale.is_sold]
        analysis = self.calculate_profit_analysis(retail_price, sold_prices)
        
        # Create summary
        summary = WatchSummary(
            model=watch_model,
            retail_price=retail_price,
            avg_sold_price=analysis.get("avg_sold_price"),
            min_sold_price=analysis.get("min_sold_price"),
            max_sold_price=analysis.get("max_sold_price"),
            recent_sales=fb_sales,
            profit_margin=analysis.get("profit_margin"),
            recommendation=analysis["recommendation"],
            suggested_buy_price=analysis.get("suggested_buy_price"),
            suggested_sell_price=analysis.get("suggested_sell_price")
        )
        
        # Cache the results (convert objects to JSON-serializable format)
        self.cached_data[watch_model] = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "model": summary.model,
                "retail_price": summary.retail_price,
                "avg_sold_price": summary.avg_sold_price,
                "min_sold_price": summary.min_sold_price,
                "max_sold_price": summary.max_sold_price,
                "profit_margin": summary.profit_margin,
                "recommendation": summary.recommendation,
                "recent_sales_count": len(summary.recent_sales)
            }
        }
        self.save_cached_data()
        
        return summary
    
    def display_summary(self, summary: WatchSummary):
        """Display formatted summary of watch pricing data"""
        print(f"\n{'='*60}")
        print(f"{Fore.CYAN}📊 WATCH PRICING SUMMARY{Style.RESET_ALL}")
        print(f"{'='*60}")
        
        print(f"\n🎯 {Style.BRIGHT}Model:{Style.RESET_ALL} {summary.model}")
        
        if summary.retail_price:
            print(f"💰 {Style.BRIGHT}Retail Price:{Style.RESET_ALL} ${summary.retail_price:,.2f}")
        
        if summary.avg_sold_price:
            print(f"\n📈 {Style.BRIGHT}Recent Sales Analysis:{Style.RESET_ALL}")
            print(f"   Average Sold Price: ${summary.avg_sold_price:,.2f}")
            print(f"   Price Range: ${summary.min_sold_price:,.2f} - ${summary.max_sold_price:,.2f}")
            
            if summary.profit_margin is not None:
                color = Fore.GREEN if summary.profit_margin > 15 else Fore.YELLOW if summary.profit_margin > 5 else Fore.RED
                print(f"   Profit Margin: {color}{summary.profit_margin:.1f}%{Style.RESET_ALL}")
        
        # Recommendation with color coding
        rec_color = Fore.GREEN if "EXCELLENT" in summary.recommendation else Fore.YELLOW if "GOOD" in summary.recommendation or "FAIR" in summary.recommendation else Fore.RED
        print(f"\n🎯 {Style.BRIGHT}Recommendation:{Style.RESET_ALL} {rec_color}{summary.recommendation}{Style.RESET_ALL}")
        
        # Show suggested buy/sell prices if available
        if summary.suggested_buy_price and summary.suggested_sell_price:
            print(f"\n💡 {Style.BRIGHT}Suggested Trading Points:{Style.RESET_ALL}")
            print(f"   Buy around: {Fore.GREEN}${summary.suggested_buy_price:,.2f}{Style.RESET_ALL}")
            print(f"   Sell around: {Fore.CYAN}${summary.suggested_sell_price:,.2f}{Style.RESET_ALL}")
            
            if summary.suggested_sell_price and summary.suggested_buy_price:
                potential_profit = summary.suggested_sell_price - summary.suggested_buy_price
                print(f"   Potential Profit: {Fore.GREEN}${potential_profit:,.2f}{Style.RESET_ALL}")
        
        if summary.recent_sales:
            max_sales = self.config.get("display", {}).get("max_recent_sales", 10)
            sales_to_show = summary.recent_sales[:max_sales]
            print(f"\n📝 {Style.BRIGHT}Recent Sales Details:{Style.RESET_ALL}")
            for i, sale in enumerate(sales_to_show, 1):
                print(f"   {i}. ${sale.price:,.2f} - {sale.condition} - {sale.date} - {sale.location}")

@click.command()
@click.argument('watch_model', required=False)
@click.option('--interactive', '-i', is_flag=True, help='Run in interactive mode')
def main(watch_model, interactive):
    """
    Watch Resell Price Tracker
    
    Track resell prices for watches from Facebook Marketplace and compare with retail prices
    to make informed buying and selling decisions.
    
    Example: python watch_tracker.py "Rolex Submariner"
    """
    print(f"\n{Fore.CYAN}⌚ Welcome to Watch Resell Price Tracker{Style.RESET_ALL}")
    print("=" * 50)
    
    tracker = WatchPriceTracker()
    
    if interactive or not watch_model:
        print("\n🔍 Enter watch models to search (type 'quit' to exit)")
        while True:
            try:
                model = input(f"\n{Fore.YELLOW}Enter watch model: {Style.RESET_ALL}").strip()
                if model.lower() in ['quit', 'exit', 'q']:
                    break
                if model:
                    summary = tracker.track_watch(model)
                    tracker.display_summary(summary)
                else:
                    print("Please enter a watch model name.")
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
                break
    else:
        summary = tracker.track_watch(watch_model)
        tracker.display_summary(summary)

if __name__ == "__main__":
    main()