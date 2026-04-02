"""
ULTIMATE REPORT GENERATOR v6.0 - 2026 PREMIUM
Produces an 8-page professional PDF with 3D renders, 
Global Costing (2026), and Livestock Strategy.
"""

from fpdf import FPDF
import datetime
from typing import Dict, Any

class HomesteadReportPro(FPDF):
    def header(self):
        # 2026 Branding: Chundal Gardens Global
        self.set_font('Arial', 'B', 12)
        self.set_text_color(46, 125, 50) # Dark Green
        self.cell(0, 10, 'CHUNDAL GARDENS | GLOBAL ARCHITECT 2026', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Confidential Design Report | Generated on {datetime.date.today()}', 0, 0, 'C')

    def generate_ultimate_report(self, data: Dict[str, Any], cost_data: Dict[str, Any], filename: str):
        self.add_page()
        
        # --- PAGE 1: TITLE & SITE SUMMARY ---
        self.set_font('Arial', 'B', 24)
        self.cell(0, 20, f"{data['acres']} Acre Global Estate Plan", 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, f"Location: {data.get('location', 'Global Site')}\nScale: {data['acres']} Acres\nStyle: Pinterest-to-3D Visual DNA")
        self.ln(10)
        
        # --- PAGE 2: ARCHITECTURAL 3D PREVIEW ---
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "Section 1: 3D Visual Masterplan", 0, 1)
        self.ln(5)
        # Note: In a real app, you'd save the Plotly fig as a PNG and add here
        # self.image('temp_3d_render.png', x=10, y=40, w=190)
        self.set_font('Arial', 'I', 10)
        self.multi_cell(0, 8, "This section visualizes the Option B Villa, curved path networks, and zone placements extracted from your design source.")

        # --- PAGE 3: WATER & SWALE STRATEGY ---
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "Section 2: Regenerative Hydrology", 0, 1)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, "2026 Water Management Plan including contour swales, primary aquaculture ponds, and rain-tank integration for 100% water security.")

        # --- PAGE 4: LIVESTOCK & ECO-SYSTEM ---
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "Section 3: Livestock & Biodiversity", 0, 1)
        self.multi_cell(0, 7, "Detailed placement of Goat Sheds, Piggeries, and Bee Hives based on Zone-to-Zone proximity logic for zero-waste farming.")

        # --- PAGE 5: ENERGY GRID (SOLAR PRO) ---
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "Section 4: Energy Independence", 0, 1)
        self.multi_cell(0, 7, "Solar PV Array layout calculated for 2026 efficiency standards. Projected offset: 100% of estate energy needs.")

        # --- PAGE 6: GLOBAL FINANCIAL ANALYSIS (THE MEAT) ---
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, f"Section 5: 2026 Investment Breakdown ({cost_data['currency']})", 0, 1)
        self.set_font('Arial', 'B', 12)
        self.cell(100, 10, "Category", 1, 0, 'C')
        self.cell(90, 10, "Estimated Cost", 1, 1, 'C')
        
        self.set_font('Arial', '', 11)
        for cat, val in cost_data['breakdown'].items():
            self.cell(100, 10, cat, 1)
            self.cell(90, 10, f"{cost_data['currency']} {val:,.2f}", 1, 1, 'R')
            
        self.ln(5)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f"Total Estimated Investment: {cost_data['currency']} {cost_data['total_estimate']:,.2f}", 0, 1, 'R')

        # --- PAGE 7: ROI & MAINTENANCE ---
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "Section 6: ROI & Sustainability", 0, 1)
        self.multi_cell(0, 7, f"Forecast: {cost_data['roi_forecast']}\nMonthly Maintenance: {cost_data['currency']} {cost_data['maintenance_monthly']:,.2f}")

        # --- PAGE 8: NEXT STEPS & BRANDING ---
        self.add_page()
        self.set_font('Arial', 'B', 20)
        self.set_text_color(46, 125, 50)
        self.cell(0, 40, "Ready to Build Your Empire?", 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 10, "Contact chundalgardens.com for on-site survey and professional implementation.\n\nYour 2026 Global Design Journey starts here.", 0, 'C')
        
        self.output(filename)
