import pytesseract
from pdf2image import convert_from_path
import cv2
import colorama
from datetime import datetime
import asyncio
from colorama import Fore
import pyfiglet
import os
import numpy
from docx import Document
colorama.init(autoreset=True)

async def image_Preproessing_threshold(img):
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return {
            "gray":gray,
            "ret":ret,
            "thresh":thresh
        }
    except Exception as ex:
        print(colorama.Fore.RED+ f"Error In Threshold Preprocessing: {ex}")
        return None
    
    
async def image_Preprocessing_Adaptive(img):
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )
        
        return {
            "gray":gray,
            "thresh": thresh
        }
        
    except Exception as ex:
        print(colorama.Fore.RED+f"Error In Adaptive Preprocessing: {ex}")
        
        
async def auto_threshold(img):
    try:

        if not isinstance(img, numpy.ndarray):
            raise ValueError("Input must be a NumPy array (image)")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        variance = numpy.var(gray)

        if variance < 500:
            return await image_Preproessing_threshold(img)
        else:
            return await image_Preprocessing_Adaptive(img)

    except Exception as ex:
        print(colorama.Fore.RED + f"Error In Auto Threshold: {ex}")
        return None




    
    
async def pdf_to_text(path, lng):
    try:
        pages = convert_from_path(path, dpi=400)
        all_texts = []

        for page in pages:
            img = numpy.array(page)
            processed = await auto_threshold(img)

            if processed is None:
                continue

            thresh_img = processed.get("thresh", processed.get("gray"))

            
            text = pytesseract.image_to_string(thresh_img, lang=lng)
            all_texts.append(text)
        filename = f"res_pdf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for t in all_texts:
                f.write(t + "\n")

        print(f"Saved to {filename}")
        return all_texts  
    except Exception as ex:
        print(f"Error in pdf_to_text: {ex}")
        return []
    
    
async def image_to_text(path, lng):
    try:
        img=cv2.imread(path)
        processed = await auto_threshold(img)
        thresh_img = processed.get("thresh", processed.get("gray"))
        
        text=pytesseract.image_to_string(thresh_img, lang=lng)
        filename = f"res_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'x', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved to {filename}")
    except Exception as ex:
        print(f"Error in image_to_text: {ex}")
        return None
    

async def word_to_text(path):
    try:
        doc = Document(path)
        text = "\n".join([p.text for p in doc.paragraphs])
       
        filename = f"res_docx_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'x', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved to {filename}")
        return text
    except Exception as ex:
        print(f"Error in word_to_text: {ex}")
        return None

async def auto_detection_type(path):
    try:
        if path.lower().endswith(".pdf"):
            print(colorama.Fore.GREEN+"-- type is pdf --")
            lng = input(colorama.Fore.GREEN+"enter pdf lang: ")
            langs_installed = pytesseract.get_languages(config='')
            print(colorama.Fore.GREEN+f"you have this langs: {langs_installed}")
            if lng in langs_installed:
                await pdf_to_text(path, lng)
            else:
                print(colorama.Fore.RED+ "You don't have installed this lang bfore!!! go and installed")
        elif path.lower().endswith(".jpg"):
            print(colorama.Fore.GREEN+"-- type is jpg --")
            lng = input(colorama.Fore.GREEN+"enter pdf lang: ")
            langs_installed = pytesseract.get_languages(config='')
            print(colorama.Fore.GREEN+f"you have this langs: {langs_installed}")
            if lng in langs_installed:
                await image_to_text(path, lng)
            else:
                print(colorama.Fore.RED+ "You don't have installed this lang bfore!!! go and installed")
            
        elif path.lower().endswith(".png"):
            print(colorama.Fore.GREEN+"-- type is jpg --")
            lng = input(colorama.Fore.GREEN+"enter pdf lang: ")
            langs_installed = pytesseract.get_languages(config='')
            print(colorama.Fore.GREEN+f"you have this langs: {langs_installed}")
            if lng in langs_installed:
                await image_to_text(path, lng)
            else:
                print(colorama.Fore.RED+ "You don't have installed this lang bfore!!! go and installed")
            
        elif path.lower().endswith(".bmp"):
            print(colorama.Fore.GREEN+"-- type is jpg --")
            lng = input(colorama.Fore.GREEN+"enter pdf lang: ")
            langs_installed = pytesseract.get_languages(config='')
            print(colorama.Fore.GREEN+f"you have this langs: {langs_installed}")
            if lng in langs_installed:
                await image_to_text(path, lng)
            else:
                print(colorama.Fore.RED+ "You don't have installed this lang bfore!!! go and installed")
            
        elif path.lower().endswith(".docx"):
            print(colorama.Fore.GREEN+"-- type is docx --")
            await word_to_text(path)

        else:
            print(colorama.Fore.RED+"-- This Type Not Supported --")
    except:
        pass
    


async def cli():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_text = pyfiglet.figlet_format("NIP-READER", font="slant")
    print(Fore.CYAN + banner_text)
    print(Fore.YELLOW + "="*80)
    print(Fore.GREEN + "Select an Option:\n")
    print(Fore.MAGENTA + "1. PDF -> Text")
    print(Fore.MAGENTA + "2. Image -> Text")
    print(Fore.MAGENTA + "3. Word -> Text")
    print(Fore.MAGENTA + "4. Exit")
    print(Fore.YELLOW + "="*80)
    while True:
        try:
            cmd = input(Fore.CYAN + "\n--->>>>> ").strip()
        
            if cmd == "1":
                path = input(Fore.YELLOW + "Enter PDF Path: ")
                await auto_detection_type(path)
                continue
            elif cmd == "2":
                path = input(Fore.YELLOW + "Enter Image Path: ")
                await auto_detection_type(path)
                continue
            elif cmd == "3":
                path = input(Fore.YELLOW + "Enter Word Path: ")
                await auto_detection_type(path)
                continue
            elif cmd == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                return Fore.CYAN + "Thanks For Running!"
            else:
                print(Fore.RED + "Command Not Recognized, Try Again!")
                await asyncio.sleep(1)
                continue
        except asyncio.exceptions.CancelledError:
            print(colorama.Fore.RED+"\t\t\t\t Please for exit type 4 don't use ctrl+c \n")
            continue
        except KeyboardInterrupt:
            print(colorama.Fore.RED+"\t\t\t\t Please for exit type 4 don't use ctrl+c \n")
            continue
        except Exception as ex:
            print(Fore.RED + f"Error in CLI: {ex}")
            return Fore.CYAN + "Thanks For Running!"



if __name__ == "__main__":
    asyncio.run(cli())