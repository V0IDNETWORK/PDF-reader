import shutil
import platform
import subprocess 
import os

def os_checker():
    os = platform.uname()[0]
    return os

def install_py_packages():
    try:
        packages = ["pytesseract", "pdf2image", "opencv-python", "colorama", "pyfiglet", "numpy", "python-docx"]

        distro = get_linux_distro()
        os_type = os_checker()

        if os_type == "Windows":
            print("⚠️ On Windows, make sure Python and pip are installed manually.")
        
        elif distro == "Debian-based":
            
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "python3-pip", "-y"], check=True)

            for pkg in packages:
                try:
                    subprocess.run(f"pip install --break-system-packages {pkg}", shell=True, check=True)
                    print(f"{pkg} installed successfully.")
                except subprocess.CalledProcessError:
                    print(f"⚠️ Failed to install {pkg}, skipping...")
        
        else:  
            for pkg in packages:
                try:
                    subprocess.run(f"pip install {pkg}", shell=True, check=True)
                    print(f"{pkg} installed successfully.")
                except subprocess.CalledProcessError:
                    print(f"⚠️ Failed to install {pkg}, skipping...")

        print("✅ Python packages installation done.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    
    
def get_linux_distro():
    try:
        with open("/etc/os-release") as f:
            data = f.read()
        if "arch" in data.lower():
            return "Arch Linux"
        elif "debian" in data.lower() or "ubuntu" in data.lower():
            return "Debian-based"
        else:
            return "Unknown Linux distro"
    except:
        return "Unknown Linux distro"
def install_ocr_langs():
    try:
        langs_input = input("Enter languages to install (e.g., fa,en,en-GB) or 'all': ").lower()
        langs_list = [l.strip() for l in langs_input.split(",") if l.strip()]

        os_type = os_checker()
        distro = get_linux_distro()

        if os_type == "Windows":
            print("⚠️ Windows detected! Please install Tesseract OCR manually from https://github.com/UB-Mannheim/tesseract/wiki")
            return

        if distro == "Arch Linux":
            subprocess.run("sudo pacman -Syu --noconfirm", shell=True, check=True)
            subprocess.run(["sudo", "pacman", "-S", "tesseract", "--noconfirm"], check=True)
            for lng in langs_list:
                try:
                    subprocess.run(["sudo", "pacman", "-S", f"tesseract-data-{lng}", "--noconfirm"], check=True)
                except subprocess.CalledProcessError:
                    print(f"⚠️ Failed to install tesseract-data-{lng}, skipping...")

        else:
            subprocess.run(["sudo", "apt", "update", "-y"], check=True)
            if "all" in langs_list:
                try:
                    subprocess.run(["sudo", "apt", "install", "tesseract-ocr-all", "-y"], check=True)
                except subprocess.CalledProcessError:
                    print("⚠️ Failed to install tesseract-ocr-all, skipping...")
            else:
                subprocess.run(["sudo", "apt", "install", "tesseract-ocr", "-y"], check=True)
                for lng in langs_list:
                    try:
                        subprocess.run(["sudo", "apt", "install", f"tesseract-ocr-{lng}", "-y"], check=True)
                    except subprocess.CalledProcessError:
                        print(f"⚠️ Failed to install tesseract-ocr-{lng}, skipping...")

        print("✅ OCR languages installation finished!")

    except Exception as e:
        print(f"Unexpected error: {e}")


    


def check_exitxs_all_files():
    try:
        files = ["gui.py", "main.py", "installer.py", "search.c"]
        miss_files = []
        for ff in files:
            if os.path.exists(ff):
                print(f"{ff} exists")
            else:
                print(f"{ff} not exists")
                miss_files.append(ff)
        if miss_files:
            print("\n⚠️ Missing files:", ", ".join(miss_files))
            return False  
        return True 
    except Exception as ex:
        print(ex)
    

def main():
    try:
        check = check_exitxs_all_files()
       
        if check:
            install_py_packages()
            install_ocr_langs()
        else:
            print("files is lost")
            
    except PermissionError:
        print("Please Run it with Permission")
    except Exception as ex:
        print(ex)
    
 
if __name__ == "__main__":
    main()