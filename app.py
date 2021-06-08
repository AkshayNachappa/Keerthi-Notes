from flask import Flask, render_template, redirect, url_for,abort

app = Flask(__name__)

sem3 = ['https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Analog_Electronics_Circuits.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Computer_Organisation_and_Architecture.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Digital_Electronics_Circuits.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Electronic_Instrumentation.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Engineering_Mathematics_III.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Network_Analysis.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/3rd_sem/Constitution_of_India.pdf']
sem4 = ['https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Electromagnetic_Field_Theory.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Engineering_Mathematics_IV.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Environmental_Studies.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Linear_Integrated_Circuits_and_Applications.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Microcontrollers.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Power_Electronics.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/4th_sem/Signals_Systems.pdf']
sem5 = ['https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/5th_sem/Analog_and_Digital_Communications.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/5th_sem/Antennas_and_Wave_Propagation.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/5th_sem/Control_Systems.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/5th_sem/Digital_Signal_Processing.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/5th_sem/Microprocessors_Systems.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/5th_sem/Operating_Systems.pdf']
sem6 = ['https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/6th_sem/Advanced_Communication_and_Coding_Theory.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/6th_sem/Data_Structures_Using_CPP.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/6th_sem/Digital_Design_using_Verilog_HDL.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/6th_sem/Digital_Switching_Systems.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/6th_sem/Embedded_Systems.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/6th_sem/Image_Processing.pdf']
sem7 = ['https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/7th_sem/CMOS_VLSI_Circuits.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/7th_sem/Communication_Networks.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/7th_sem/Internet_of_Things.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/7th_sem/Microwaves_and_Radar.pdf', 'https://drive.google.com/viewerng/viewer?embedded=true&url=https://AkshayNachappa.github.io/Keerthi_Notes_Compressed/7th_sem/Wireless_Communications.pdf']
sems = [sem3,sem4,sem5,sem6,sem7]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")    

@app.route("/BE")
def BE():
    return render_template("BE-main.html")

@app.route("/BE/<int:sem_no>")
def BE_sems(sem_no):
    if(sem_no>7 or sem_no<3):
        abort(404)
    names = []
    links = sems[sem_no - 3]
    for link in links:
        names.append(link[slice(125,link.find('.pdf'))].replace('_',' '))

    return render_template("BE-sems.html",sem_no=sem_no,links=links,names=names,zip=zip)

if __name__ == '__main__':
    app.run(debug=False)





