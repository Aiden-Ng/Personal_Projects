import requests
import openpyxl 
from bs4 import BeautifulSoup as bs 
import re 

##
#   @mainpage Doxygen Documentation for NTUSU food recommendation 
#   @section main_description Description
#   This projects aims to scrap restaurant data from website and put it into a ExcelSheet 
#   @section main_note Notes 
#   sN/A 



##
#   @brief Defines the code for web scrapping 
#
#   @section description_web_scraping_NTUSU Description 
#   This is a web scrapping project to scrap the best eats in Singapore
#
#   @section note_web_scraping_NTUSU_description Notes 
#   This is the code section
#
# 

website_url = "https://www.timeout.com/singapore/restaurants/best-cheap-eats-in-singapore"
excel_path  = r"C:\Users\Ng Hong Xi\Desktop\Food_recommendation_for_NTUSU.xlsx"

def main():
    """!This is the entry point     
    """
    website = requests.get(website_url)
    website_html = bs(website.text, "html.parser")
    website_html_image_tag = website_html.find_all('div', attrs={'class': '_imageWrap_vapn8_242'})
    website_html_data_srcset_attrs = srcset_string_get(website_html_image_tag_args =  website_html_image_tag)
    website_html_data_srcset_attrs = srcset_string_get(website_html_image_tag_args =  website_html_image_tag[0].img["data-srcset"])
    
    ##JOHANSON

    #split the srcset string into an array
    data_srcset_split_array = website_html_data_srcset_attrs.split(",")
    #function call 
    image_text = find_ideal_image_size_http_link(required_size = "380w", srcset_array = data_srcset_split_array)
    print(image_text)

#working correctly 
def srcset_string_get(*, website_html_image_tag_args = "None"):
    '''!This gets the lazy loading image srouce 

    @param website_html_image_tag_args This is the <img> tag for the html 
    @return The <img> tag srcset attributes
     '''
    website_image_tag_srcset_attrs = website_html_image_tag_args[0].img["data-srcset"]
    return website_image_tag_srcset_attrs

#sets 380 as default 
def find_ideal_image_size_http_link(*, required_size = "380", srcset_array = "None"):
    '''!This gets the exact image http link

    @param required_size This is the width of the image
    @param srcset_array This is the array of the srcset attributes

    @return The http link of the image
    '''
    #goes through the array and finds the image with 380w size
    for i in range (len(srcset_array)):
    #returns the Match object of this re
        search_status = re.search( required_size, srcset_array[i])
        if search_status is not None:
        #this obtains the first image of 380w
            return (search_status.string.split(" ")[0])





    
    
    
    
    
    
    
    
    
    
    
    


    
    
def excel_handler():
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active 
    wb.save(excel_path)
    
    
#excel_handler()
main()



