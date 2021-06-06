from flask import Flask, render_template, redirect, url_for,abort

app = Flask(__name__)

sem3 = ['https://AkshayNachappa.github.io/Keerthi_Notes/3rd_Sem/Analog_Electronics_Circuits.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/3rd_Sem/Computer_Organisation_and_Architecture.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/3rd_Sem/Digital_Electronics_Circuits.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/3rd_Sem/Electronic_Instrumentation.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/3rd_Sem/Engineering_Mathematics_III.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/3rd_Sem/Network_Analysis.pdf']
sem4 = ['https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Electromagnetic_Field_Theory.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Engineering_Mathematics_IV.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Environmental_Studies.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Linear_Integrated_Circuits_and_Applications.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Microcontrollers.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Power_Electronics.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/4th_Sem/Signals_Systems.pdf']
sem5 = ['https://AkshayNachappa.github.io/Keerthi_Notes/5th_Sem/Analog_and_Digital_Communications.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/5th_Sem/Antennas_and_Wave_Propagation.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/5th_Sem/Control_Systems.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/5th_Sem/Digital_Signal_Processing.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/5th_Sem/Microprocessors_Systems.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/5th_Sem/Operating_Systems.pdf']
sem6 = ['https://AkshayNachappa.github.io/Keerthi_Notes/6th_Sem/Advanced_Communication_and_Coding_Theory.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/6th_Sem/Data_Structures_Using_CPP.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/6th_Sem/Digital_Design_using_Verilog_HDL.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/6th_Sem/Digital_Switching_Systems.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/6th_Sem/Embedded_Systems.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/6th_Sem/Image_Processing.pdf']
sem7 = ['https://AkshayNachappa.github.io/Keerthi_Notes/7th_Sem/CMOS_VLSI_Circuits.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/7th_Sem/Communication_Networks.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/7th_Sem/Internet_of_Things.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/7th_Sem/Microwaves_and_Radar.pdf', 'https://AkshayNachappa.github.io/Keerthi_Notes/7th_Sem/Wireless_Communications.pdf']
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
    if(sem_no>7):
        abort(404)
    names = []
    links = sems[sem_no - 3]
    for link in links:
        names.append(link[slice(55,link.find('.pdf'))].replace('_',' '))

    return render_template("BE-sems.html",sem_no=sem_no,links=links,names=names,zip=zip)

if __name__ = '__main__':
    app.run(debug=False)





