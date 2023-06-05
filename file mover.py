import os, shutil, time #importing useful modules
moveTo = os.path.expanduser("~") #The path to find where to move your file to
downloadDir = os.path.expanduser("~\Downloads") #path to downloads

#function for moving
def moving():
     print("This is the list of all the files in your downloads\n")
     time.sleep(2)
     for i in os.listdir(downloadDir):
          print(i) #listing all the files in downloads
     fileMove = input("\nType the name of the file to copy\n")
     #checking if the input is in the Downloads directory
     
     for i in os.listdir(downloadDir): #This loop will continue as long as it finds a fille or folder that starts with users input 
          if i.startswith(fileMove):
               print(i + "\n")  
               pasting(i) #move over to the paste function

#function for pasting      
def pasting(fileToMove):
     moveFolders = os.listdir(moveTo) #list of all items in moveTo path
     time.sleep(2)
     for filename in moveFolders: #loop through the moveTo path 
          if os.path.isdir(os.path.join(moveTo,filename)): #intelligently join path and filename
               print(filename) # only print out the filename 
     folder = input("Please which folder are you moving your file to?\n") #get user folder input
     if folder in moveFolders:     #while looping, check if input is in moveFolders
          docDir = os.listdir(os.path.expanduser("~\\"+folder))  #append folder to path
          for docFolder in docDir: #open the folder 
               print(docFolder)
          docIn = input("Which folder please or type STOP or press Enter to paste here\n") #ask for user input to folder you want to paste
          pasteDir = os.path.expanduser("~\\" + folder)
          if docIn in docDir: #else paste it in the folder typed by the user 
               shutil.move(os.path.expanduser("~\Downloads\\"+ fileToMove), pasteDir + "\\" + docIn)
          else: #if user type stop, program should paste it here 
               shutil.move(os.path.expanduser("~\Downloads\\"+ fileToMove), pasteDir)
     else :
          print("\nWrong Input\n")
          pasting(fileToMove)

def main():
     #Get what user wants to do 
     print("""How do you want to move files?
All musics - type music
All videos,movies - type videos
All pdfs - type pdfs
All zips - type zips
All pictures - type pics
All software - type softs
If you want to do it manually - type manual
If you are lazy to arrange your downloaded items to their respective(allow our machine to do it for you) - type arrange\n""")
     toDo = input()
     match toDo.lower():
          
          case "arrange":
               for i in os.listdir(downloadDir):
                    arrange(i)
          
          case 'manual':
               moving()

          #Moves all music to Music Directory 
          case 'music':
               for i in os.listdir(downloadDir):
                    if i.endswith(".mp3") | i.endswith(".m4a") | i.endswith(".wav")| i.endswith(".flac")| i.endswith(".aac")| i.endswith(".ogg")| i.endswith(".wma")| i.endswith("aiff") | i.endswith(".mid"):
                         shutil.move(os.path.expanduser("~\Downloads\\" + i), os.path.expanduser("~\Music"))

          #Moves all videos to Video Directory
          case 'videos':
               for i in os.listdir(downloadDir):
                    if i.endswith(".mkv") | i.endswith(".mp4")|i.endswith( ".avi") | i.endswith(".mov") | i.endswith(".wmv") | i.endswith(".flv") |i.endswith(".mpg")| i.endswith("mpeg") | i.endswith(".3gp"):
                         shutil.move(os.path.expanduser("~\Downloads\\" + i), os.path.expanduser("~\Videos"))

          #Move all pdfs to PDFs directory
          case 'pdfs':
               for i in os.listdir(downloadDir):
                    if i.endswith(".pdf"):
                         if "PDFs" in os.listdir(os.path.expanduser("~\Documents")): #checks if directory exist
                              shutil.move(os.path.expanduser("~\Downloads\\" + i),os.path.expanduser("~\Documents\PDFs"))
                         else: #creates a new directory if it doesn't exist
                              os.mkdir(os.path.expanduser("~\Documents\PDFs"))
                              shutil.move(os.path.expanduser("~\Downloads\\" + i),os.path.expanduser("~\Documents\PDFs"))

           #Move all compressed files to ZIPs folder         
          case 'zips':
               for i in os.listdir(downloadDir):
                    if i.endswith(".zip")| i.endswith(".rar")| i.endswith(".7z"):
                         if "ZIPs" in os.listdir(os.path.expanduser("~\Documents")): #checks if directory exist
                              shutil.move(os.path.expanduser("~\Downloads\\" + i),os.path.expanduser("~\Documents\ZIPs"))
                         else: #creates a new directory if it doesn't exist
                              os.mkdir(os.path.expanduser("~\Documents\ZIPs"))
                              shutil.move(os.path.expanduser("~\Downloads\\" + i),os.path.expanduser("~\Documents\ZIPs"))
                    
          case 'pics':
               for i in os.listdir(downloadDir):
                    if i.endswith(".png")|i.endswith(".gif")|i.endswith(".bmp")|i.endswith("jpeg")|i.endswith(".jpg")|i.endswith(".raw")|i.endswith(".svg")|i.endswith(".JPG"):
                         shutil.move(os.path.expanduser("~\Downloads\\" + i), os.path.expanduser("~\Pictures"))

          #Move all executable files to Software folder
          case 'softs':
               for i in os.listdir(downloadDir):
                    if i.endswith(".exe")|i.endswith(".msi"):
                         if "Softwares" in os.listdir(os.path.expanduser("~\Documents")): #checks if directory exist
                              shutil.move(os.path.expanduser("~\Downloads\\" + i),os.path.expanduser("~\Documents\Softwares"))
                         else: #creates a new directory if it doesn't exist
                              os.mkdir(os.path.expanduser("~\Documents\Softwares"))
                              shutil.move(os.path.expanduser("~\Downloads\\" + i),os.path.expanduser("~\Documents\Softwares"))

          #Runs code again if input is invalid
          case _ :
               print("Wrong Input")
               main()

     print("Done")

      
def arrange(file):
     fileExe = file[-4:]
     match fileExe:
          case ".mp3" | ".m4a" | ".wav"|".flac"| ".aac"|".ogg"|".wma"|"aiff" | ".mid":
               shutil.move(os.path.expanduser("~\Downloads\\" +file), os.path.expanduser("~\Musics"))
               
          case ".mkv" | ".mp4"| ".avi" | ".mov" | ".wmv" | ".flv" |".mpg"| "mpeg" | ".3gp":
               shutil.move(os.path.expanduser("~\Downloads\\" +file), os.path.expanduser("~\Videos"))
               
          case ".png"| ".gif"| ".bmp" | ".tif" | "tiff"| ".raw"| ".svg"| ".JPG" | "JPEG"| ".jpg"| "jpeg" :
               shutil.move(os.path.expanduser("~\Downloads\\" +file), os.path.expanduser("~\Pictures"))
               
          case ".pdf" :
               if "PDFs" in os.listdir(os.path.expanduser("~\Documents")): #checks if directory exist
                    shutil.move(os.path.expanduser("~\Downloads\\" + file),os.path.expanduser("~\Documents\PDFs"))
               else: #creates a new directory if it doesn't exist
                    os.mkdir(os.path.expanduser("~\Documents\PDFs"))
                    shutil.move(os.path.expanduser("~\Downloads\\" + file),os.path.expanduser("~\Documents\PDFs"))
                    
          case ".zip"|".rar" :
               if "ZIPs" in os.listdir(os.path.expanduser("~\Documents")):#checks if directory exist
                    shutil.move(os.path.expanduser("~\Downloads\\" + file), os.path.expanduser("~\Documents\ZIPs"))
               else: #creates a new directory if it doesn't exist
                    os.mkdir(os.path.expanduser("~\Documents\ZIPs"))
                    shutil.move(os.path.expanduser("~\Downloads\\" + file), os.path.expanduser("~\Documents\ZIPs"))
                    
          case _ :
               print(file)
               if file == "desktop.ini":
                    print("skipped, Not to be moved")
               else:
                    ques = input("Is this a folder or software?\n Software - type soft\n folder - type folder\n Or just press Enter\n")
                    if ques.lower() == "soft":
                         if "Softwares" in os.listdir(os.path.expanduser("~\Documents")): #checks if directory exist
                              shutil.move(os.path.expanduser("~\Downloads\\" + file),os.path.expanduser("~\Documents\Softwares"))
                         else: #creates a new directory if it doesn't exist
                              os.mkdir(os.path.expanduser("~\Documents\Softwares"))
                              shutil.move(os.path.expanduser("~\Downloads\\" + file),os.path.expanduser("~\Documents\Softwares"))
                              
                    elif ques.lower() == "folder":
                         shutil.move(os.path.expanduser("~\Downloads\\" +file),os.path.expanduser("~\Documents"))
                    else:
                         shutil.move(os.path.expanduser("~\Downloads\\" +file),os.path.expanduser("~\Documents"))
    
try:
     print("At any point, to exit Press CTRL + C")
     time.sleep(2)
     if __name__ == "__main__":
         main()
except KeyboardInterrupt:
     print("Program closed")

     
     
