import openpyxl as op


excel_path = "C://Users//Ng Hong Xi//Desktop//Food_recommendation_for_NTUSU.xlsx"
def main():
    excel = op.load_workbook(excel_path)
    ws = excel.active 
    ws["A1"] = "Lanjiaos"
    excel.save()

main()