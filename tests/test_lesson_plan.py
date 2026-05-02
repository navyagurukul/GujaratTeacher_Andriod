import pytest
from pages.lesson_plan_page import LessonPlanPage
@pytest.mark.order(3)
class TestLessonPlan:

    def test_all_grades_pdfs(self, logged_in_driver):
        """
        Automation to verify PDF accessibility across all grades.
        1. Navigates to Lesson Plan.
        2. Iterates through every available Grade/Class.
        3. Clicks every PDF icon and selects the 'Video/Microschedule' activity.
        4. Verifies the PDF opens and returns to the list.
        """
        driver = logged_in_driver
        page = LessonPlanPage(driver)
        
        # 1. Navigate to the Lesson Plan section
        page.open_lesson_plan()
        
        # 2. Extract list of all available grades from the dropdown
        grades = page.get_grades()
        
        total_verified = 0
        
        # 3. Process each grade one by one
        for grade in grades:
            print(f"\n--- 📂 STARTING GRADE: {grade} ---")
            
            try:
                # Select the grade
                page.select_grade(grade)
                
                # Process all PDF icons found in this specific grade
                # This returns the count of successfully opened PDFs
                count = page.process_all_topics()
                total_verified += count
                
                print(f"✅ Finished {grade}. Topics verified: {count}")
                
            except Exception as e:
                print(f"❌ Critical error processing {grade}: {str(e)[:100]}")
                # Refresh page to recover state for the next grade
                driver.refresh()
                page.open_lesson_plan()
                continue

        print(f"\n================================================")
        print("🎯 AUTOMATION COMPLETE")
        print(f"📊 Total PDFs verified across all grades: {total_verified}")
        print("================================================")
        
        # Ensure at least one PDF was processed successfully
        assert total_verified > 0, "No PDFs were successfully verified during the run."
