## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain.document_loaders import PDFLoader

## ✅ Search Tool using Serper
search_tool = SerperDevTool()

## ✅ Custom Blood Test PDF Reader Tool
class BloodTestReportTool:
    @property
    def read_data_tool(self):
        """Tool to read and clean data from a blood test PDF report"""

        async def _read_data_tool(path: str = 'data/sample.pdf') -> str:
            try:
                docs = PDFLoader(file_path=path).load()
            except Exception as e:
                return f"Failed to read PDF file at {path}. Error: {e}"

            full_report = ""

            for data in docs:
                content = data.page_content.strip()
                # Normalize whitespace and format
                cleaned = "\n".join(
                    [line.strip() for line in content.splitlines() if line.strip()]
                )
                full_report += cleaned + "\n"

            return full_report.strip()

        return _read_data_tool

## ✅ Nutrition Analysis Tool Template
class NutritionTool:
    @property
    def analyze_nutrition_tool(self):
        async def _analyze(blood_report_data: str) -> str:
            # Clean extra spaces
            processed = " ".join(blood_report_data.split())

            # TODO: Add actual logic here
            return (
                "🧪 Nutrition analysis (placeholder):\n"
                f"Processed summary: {processed[:150]}...\n"
                "More insights will be implemented here."
            )

        return _analyze

## ✅ Exercise Planning Tool Template
class ExerciseTool:
    @property
    def create_exercise_plan_tool(self):
        async def _create_plan(blood_report_data: str) -> str:
            # TODO: Add actual logic here
            return (
                "🏋️ Exercise planning (placeholder):\n"
                "Plan generation logic will be implemented here."
            )

        return _create_plan
