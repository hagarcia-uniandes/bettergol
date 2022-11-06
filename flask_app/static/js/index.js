clasificadosa = [];
clasificadosb = [];
clasificadosc = [];
clasificadosd = [];
clasificadose = [];
clasificadosf = [];
clasificadosg = [];
clasificadosh = [];
//*Grupo A
function grupoa(elemento){
const pais1 = document.querySelector('.a1');
const pais2 = document.querySelector('.a2');
const pais3 = document.querySelector('.a3');
const pais4 = document.querySelector('.a4');
    clasificadosa.push(elemento.value);
    if(clasificadosa.includes('QAT')){
        pais1.disabled = true;
    }
    if(clasificadosa.includes('ECU')){
        pais2.disabled = true;
    }
    if(clasificadosa.includes('SEN')){
        pais3.disabled = true;
    }
    if(clasificadosa.includes('HOL')){
        pais4.disabled = true;
    }
    const a1 = clasificadosa[0];
    const a2 = clasificadosa[1];
    console.log(a1,a2)
    if(clasificadosa.length >= 2){
        pais1.disabled = true;
        pais2.disabled = true;
        pais3.disabled = true;
        pais4.disabled = true;
        
    }

    //Pruebas estilos 1 y 2
    if(elemento.value == a1){
        elemento.classList.add("numero1");
    }
    if(elemento.value == a2){
        elemento.classList.add("numero2")
    }
    document.getElementById("CA1").innerHTML = `${a1} <img class="float-end" src="static/img/${a1}.svg" width="25">`;
    document.getElementById("CA2").innerHTML = `${a2} <img class="float-end" src="static/img/${a2}.svg" width="25">`;
    document.getElementById("A1").value = a1;
    document.getElementById("A2").value = a2;
    //Hidden inputs equipos primeros y segundos de cada grupo
    document.getElementById("ha1").value = a1;
    document.getElementById("ha2").value = a2;

    if(a1){
        document.getElementById("A1").disabled = false
    }
    if(a2){
        document.getElementById("A2").disabled = false
    }
}
//*Reiniciar A
function reiniciara(){
    const pais1 = document.querySelector('.a1');
    const pais2 = document.querySelector('.a2');
    const pais3 = document.querySelector('.a3');
    const pais4 = document.querySelector('.a4');
    clasificadosa = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("A1").disabled = true;
    document.getElementById("A2").disabled = true;
    document.getElementById("CA1").innerText = "A1";
    document.getElementById("CA2").innerText = "A2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo B
function grupob(elemento){
    const pais1 = document.querySelector('.b1');
    const pais2 = document.querySelector('.b2');
    const pais3 = document.querySelector('.b3');
    const pais4 = document.querySelector('.b4');
        clasificadosb.push(elemento.value);
        if(clasificadosb.includes('ING')){
            pais1.disabled = true;
        }
        if(clasificadosb.includes('IRA')){
            pais2.disabled = true;
        }
        if(clasificadosb.includes('USA')){
            pais3.disabled = true;
        }
        if(clasificadosb.includes('GAL')){
            pais4.disabled = true;
        }
        const b1 = clasificadosb[0];
        const b2 = clasificadosb[1];
        console.log(b1,b2)
        if(clasificadosb.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }
        if(elemento.value == b1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == b2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CB1").innerHTML = `<img class="float-start" src="static/img/${b1}.svg" width="25"> ${b1}`;
        document.getElementById("CB2").innerHTML = `<img class="float-start" src="static/img/${b2}.svg" width="25"> ${b2}`;
        document.getElementById("B1").value = b1;
        document.getElementById("B2").value = b2;

        document.getElementById("hb1").value = b1;
        document.getElementById("hb2").value = b2;

        if(b1){
            document.getElementById("B1").disabled = false
        }
        if(b2){
            document.getElementById("B2").disabled = false
        }
    }

//*Reiniciar B
function reiniciarb(){
    const pais1 = document.querySelector('.b1');
    const pais2 = document.querySelector('.b2');
    const pais3 = document.querySelector('.b3');
    const pais4 = document.querySelector('.b4');
    clasificadosb = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("B1").disabled = true;
    document.getElementById("B2").disabled = true;
    document.getElementById("CB1").innerText = "B1";
    document.getElementById("CB2").innerText = "B2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo C
function grupoc(elemento){
    const pais1 = document.querySelector('.c1');
    const pais2 = document.querySelector('.c2');
    const pais3 = document.querySelector('.c3');
    const pais4 = document.querySelector('.c4');
        clasificadosc.push(elemento.value);
        if(clasificadosc.includes('ARG')){
            pais1.disabled = true;
        }
        if(clasificadosc.includes('ARA')){
            pais2.disabled = true;
        }
        if(clasificadosc.includes('MEX')){
            pais3.disabled = true;
        }
        if(clasificadosc.includes('POL')){
            pais4.disabled = true;
        }
        const c1 = clasificadosc[0];
        const c2 = clasificadosc[1];
        console.log(c1,c2)
        if(clasificadosc.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }

        if(elemento.value == c1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == c2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CC1").innerHTML = `${c1} <img class="float-end" src="static/img/${c1}.svg" width="25">`;
        document.getElementById("CC2").innerHTML = `${c2} <img class="float-end" src="static/img/${c2}.svg" width="25">`;
        document.getElementById("C1").value = c1;
        document.getElementById("C2").value = c2;

        document.getElementById("hc1").value = c1;
        document.getElementById("hc2").value = c2;

        if(c1){
            document.getElementById("C1").disabled = false
        }
        if(c2){
            document.getElementById("C2").disabled = false
        }
    }

//*Reiniciar C
function reiniciarc(){
    const pais1 = document.querySelector('.c1');
    const pais2 = document.querySelector('.c2');
    const pais3 = document.querySelector('.c3');
    const pais4 = document.querySelector('.c4');
    clasificadosc = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("C1").disabled = true;
    document.getElementById("C2").disabled = true;
    document.getElementById("CC1").innerText = "C1";
    document.getElementById("CC2").innerText = "C2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo D
function grupod(elemento){
    const pais1 = document.querySelector('.d1');
    const pais2 = document.querySelector('.d2');
    const pais3 = document.querySelector('.d3');
    const pais4 = document.querySelector('.d4');
        clasificadosd.push(elemento.value);
        if(clasificadosd.includes('FRA')){
            pais1.disabled = true;
        }
        if(clasificadosd.includes('AUS')){
            pais2.disabled = true;
        }
        if(clasificadosd.includes('DIN')){
            pais3.disabled = true;
        }
        if(clasificadosd.includes('TUN')){
            pais4.disabled = true;
        }
        const d1 = clasificadosd[0];
        const d2 = clasificadosd[1];
        console.log(d1,d2)
        if(clasificadosd.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }
        
        if(elemento.value == d1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == d2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CD1").innerHTML = `<img class="float-start" src="static/img/${d1}.svg" width="25"> ${d1}`;
        document.getElementById("CD2").innerHTML = `<img class="float-start" src="static/img/${d2}.svg" width="25"> ${d2}`;
        document.getElementById("D1").value = d1;
        document.getElementById("D2").value = d2;

        document.getElementById("hd1").value = d1;
        document.getElementById("hd2").value = d2;

        if(d1){
            document.getElementById("D1").disabled = false
        }
        if(d2){
            document.getElementById("D2").disabled = false
        }
    }
//*Reiniciar D
function reiniciard(){
    const pais1 = document.querySelector('.d1');
    const pais2 = document.querySelector('.d2');
    const pais3 = document.querySelector('.d3');
    const pais4 = document.querySelector('.d4');
    clasificadosd = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("D1").disabled = true;
    document.getElementById("D2").disabled = true;
    document.getElementById("CD1").innerText = "D1";
    document.getElementById("CD2").innerText = "D2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo E
function grupoe(elemento){
    const pais1 = document.querySelector('.e1');
    const pais2 = document.querySelector('.e2');
    const pais3 = document.querySelector('.e3');
    const pais4 = document.querySelector('.e4');
        clasificadose.push(elemento.value);
        if(clasificadose.includes('ESP')){
            pais1.disabled = true;
        }
        if(clasificadose.includes('CRI')){
            pais2.disabled = true;
        }
        if(clasificadose.includes('ALE')){
            pais3.disabled = true;
        }
        if(clasificadose.includes('JAP')){
            pais4.disabled = true;
        }
        const e1 = clasificadose[0];
        const e2 = clasificadose[1];
        console.log(e1,e2)
        if(clasificadose.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }
        

        if(elemento.value == e1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == e2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CE1").innerHTML = `${e1} <img class="float-end" src="static/img/${e1}.svg" width="25">`;
        document.getElementById("CE2").innerHTML = `${e2} <img class="float-end" src="static/img/${e2}.svg" width="25">`;
        document.getElementById("E1").value = e1;
        document.getElementById("E2").value = e2;

        document.getElementById("he1").value = e1;
        document.getElementById("he2").value = e2;

        if(e1){
            document.getElementById("E1").disabled = false
        }
        if(e2){
            document.getElementById("E2").disabled = false
        }
    }

//*Reiniciar E
function reiniciare(){
    const pais1 = document.querySelector('.e1');
    const pais2 = document.querySelector('.e2');
    const pais3 = document.querySelector('.e3');
    const pais4 = document.querySelector('.e4');
    clasificadose = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("E1").disabled = true;
    document.getElementById("E2").disabled = true;
    document.getElementById("CE1").innerText = "E1";
    document.getElementById("CE2").innerText = "E2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo F
function grupof(elemento){
    const pais1 = document.querySelector('.f1');
    const pais2 = document.querySelector('.f2');
    const pais3 = document.querySelector('.f3');
    const pais4 = document.querySelector('.f4');
        clasificadosf.push(elemento.value);
        if(clasificadosf.includes('BEL')){
            pais1.disabled = true;
        }
        if(clasificadosf.includes('CAN')){
            pais2.disabled = true;
        }
        if(clasificadosf.includes('MAR')){
            pais3.disabled = true;
        }
        if(clasificadosf.includes('CRO')){
            pais4.disabled = true;
        }
        const f1 = clasificadosf[0];
        const f2 = clasificadosf[1];
        console.log(f1,f2)
        if(clasificadosf.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }

        

        if(elemento.value == f1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == f2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CF1").innerHTML = `<img class="float-start" src="static/img/${f1}.svg" width="25"> ${f1}`;
        document.getElementById("CF2").innerHTML = `<img class="float-start" src="static/img/${f2}.svg" width="25"> ${f2}`;
        document.getElementById("F1").value = f1;
        document.getElementById("F2").value = f2;

        document.getElementById("hf1").value = f1;
        document.getElementById("hf2").value = f2;

        if(f1){
            document.getElementById("F1").disabled = false
        }
        if(f2){
            document.getElementById("F2").disabled = false
        }
    }

//*Reiniciar F
function reiniciarf(){
    const pais1 = document.querySelector('.f1');
    const pais2 = document.querySelector('.f2');
    const pais3 = document.querySelector('.f3');
    const pais4 = document.querySelector('.f4');
    clasificadosf = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("F1").disabled = true;
    document.getElementById("F2").disabled = true;
    document.getElementById("CF1").innerText = "F1";
    document.getElementById("CF2").innerText = "F2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo G
function grupog(elemento){
    const pais1 = document.querySelector('.g1');
    const pais2 = document.querySelector('.g2');
    const pais3 = document.querySelector('.g3');
    const pais4 = document.querySelector('.g4');
        clasificadosg.push(elemento.value);
        if(clasificadosg.includes('BRA')){
            pais1.disabled = true;
        }
        if(clasificadosg.includes('SER')){
            pais2.disabled = true;
        }
        if(clasificadosg.includes('SUI')){
            pais3.disabled = true;
        }
        if(clasificadosg.includes('CAM')){
            pais4.disabled = true;
        }
        const g1 = clasificadosg[0];
        const g2 = clasificadosg[1];
        console.log(g1,g2)
        if(clasificadosg.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }
        
        if(elemento.value == g1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == g2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CG1").innerHTML = `${g1} <img class="float-end" src="static/img/${g1}.svg" width="25">`;
        document.getElementById("CG2").innerHTML = `${g2} <img class="float-end" src="static/img/${g2}.svg" width="25">`;
        document.getElementById("G1").value = g1;
        document.getElementById("G2").value = g2;

        document.getElementById("hg1").value = g1;
        document.getElementById("hg2").value = g2;

        if(g1){
            document.getElementById("G1").disabled = false
        }
        if(g2){
            document.getElementById("G2").disabled = false
        }
    }

//*Reiniciar G
function reiniciarg(){
    const pais1 = document.querySelector('.g1');
    const pais2 = document.querySelector('.g2');
    const pais3 = document.querySelector('.g3');
    const pais4 = document.querySelector('.g4');
    clasificadosg = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("G1").disabled = true;
    document.getElementById("G2").disabled = true;
    document.getElementById("CG1").innerText = "G1";
    document.getElementById("CG2").innerText = "G2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

//*Grupo H
function grupoh(elemento){
    const pais1 = document.querySelector('.hh1');
    const pais2 = document.querySelector('.hh2');
    const pais3 = document.querySelector('.hh3');
    const pais4 = document.querySelector('.hh4');
        clasificadosh.push(elemento.value);
        if(clasificadosh.includes('POR')){
            pais1.disabled = true;
        }
        if(clasificadosh.includes('GHA')){
            pais2.disabled = true;
        }
        if(clasificadosh.includes('URU')){
            pais3.disabled = true;
        }
        if(clasificadosh.includes('CSR')){
            pais4.disabled = true;
        }
        const h1 = clasificadosh[0];
        const h2 = clasificadosh[1];
        console.log(h1,h2)
        if(clasificadosh.length >= 2){
            pais1.disabled = true;
            pais2.disabled = true;
            pais3.disabled = true;
            pais4.disabled = true;
            
        }


        if(elemento.value == h1){
            elemento.classList.add("numero1");
        }
        if(elemento.value == h2){
            elemento.classList.add("numero2")
        }
        
        document.getElementById("CH1").innerHTML = `<img class="float-start" src="static/img/${h1}.svg" width="25"> ${h1}`;
        document.getElementById("CH2").innerHTML = `<img class="float-start" src="static/img/${h2}.svg" width="25"> ${h2}`;
        document.getElementById("H1").value = h1;
        document.getElementById("H2").value = h2;

        document.getElementById("hh1").value = h1;
        document.getElementById("hh2").value = h2;

        if(h1){
            document.getElementById("H1").disabled = false
        }
        if(h2){
            document.getElementById("H2").disabled = false
        }
        
    }

//*Reiniciar H
function reiniciarh(){
    const pais1 = document.querySelector('.hh1');
    const pais2 = document.querySelector('.hh2');
    const pais3 = document.querySelector('.hh3');
    const pais4 = document.querySelector('.hh4');
    clasificadosh = [];
    pais1.disabled = false;
    pais2.disabled = false;
    pais3.disabled = false;
    pais4.disabled = false;
    document.getElementById("H1").disabled = true;
    document.getElementById("H2").disabled = true;
    document.getElementById("CH1").innerText = "H1";
    document.getElementById("CH2").innerText = "H2";
    pais1.classList.remove("numero1");
    pais1.classList.remove("numero2");
    pais2.classList.remove("numero1");
    pais2.classList.remove("numero2");
    pais3.classList.remove("numero1");
    pais3.classList.remove("numero2");
    pais4.classList.remove("numero1");
    pais4.classList.remove("numero2");
}

function octavos(id){
    let pais = document.querySelector(id);
    if(pais.id == "A1" || pais.id == "B2"){
        document.getElementById("CO1").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("O1").value = pais.value;
        //if y variable para activar y desactivar los botones
        const o1 = pais.value;
        if(o1){
            document.getElementById("O1").disabled = false;
        }
    }
    if(pais.id == "C1" || pais.id == "D2"){
        document.getElementById("CO2").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("O2").value = pais.value;
        const o2 = pais.value;
        if(o2){
            document.getElementById("O2").disabled = false;
        }
    }
    if(pais.id == "E1" || pais.id == "F2"){
        document.getElementById("CO3").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("O3").value = pais.value;
        const o3 = pais.value;
        if(o3){
            document.getElementById("O3").disabled = false;
        }
    }
    if(pais.id == "G1" || pais.id == "H2"){
        document.getElementById("CO4").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("O4").value = pais.value;
        const o4 = pais.value;
        if(o4){
            document.getElementById("O4").disabled = false;
        }
    }
    if(pais.id == "A2" || pais.id == "B1"){
        document.getElementById("CO5").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("O5").value = pais.value;
        const o5 = pais.value;
        if(o5){
            document.getElementById("O5").disabled = false;
        }
    }
    if(pais.id == "C2" || pais.id == "D1"){
        document.getElementById("CO6").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("O6").value = pais.value;
        const o6 = pais.value;
        if(o6){
            document.getElementById("O6").disabled = false;
        }
    }
    if(pais.id == "E2" || pais.id == "F1"){
        document.getElementById("CO7").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("O7").value = pais.value;
        const o7 = pais.value;
        if(o7){
            document.getElementById("O7").disabled = false;
        }
    }
    if(pais.id == "G2" || pais.id == "H1"){
        document.getElementById("CO8").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("O8").value = pais.value;
        const o8 = pais.value;
        if(o8){
            document.getElementById("O8").disabled = false;
        }
    }
    
}

function cuartos(id){
    let pais = document.querySelector(id);
    if(pais.id == "O1" || pais.id == "O2"){
        document.getElementById("CSEMI1").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("SEMIC1").value = pais.value;
        const semi1 = pais.value;
        if(semi1){
            document.getElementById("SEMIC1").disabled = false;
        }
    }
    if(pais.id == "O3" || pais.id == "O4"){
        document.getElementById("CSEMI2").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("SEMIC2").value = pais.value;
        const semi2 = pais.value;
        if(semi2){
            document.getElementById("SEMIC2").disabled = false;
        }
    }
    if(pais.id == "O5" || pais.id == "O6"){
        document.getElementById("CSEMI3").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("SEMIC3").value = pais.value;
        const semi3= pais.value;
        if(semi3){
            document.getElementById("SEMIC3").disabled = false;
        }
    }
    if(pais.id == "O7" || pais.id == "O8"){
        document.getElementById("CSEMI4").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("SEMIC4").value = pais.value;
        const semi4 = pais.value;
        if(semi4){
            document.getElementById("SEMIC4").disabled = false;
        }
    }
}

function semis(id){
    let pais = document.querySelector(id);
    if(pais.id == "SEMIC1" || pais.id == "SEMIC2"){
        document.getElementById("Lfinal1").innerHTML = `${pais.value} <img class="float-end" src="static/img/${pais.value}.svg" width="25">`;
        document.getElementById("final1").value = pais.value;
        const final1 = pais.value;
        if(final1){
            document.getElementById("final1").disabled = false;
        }
        if(pais.value == SEMIC1.value){
            document.getElementById("LPS1").innerHTML = `${SEMIC2.value} <img class="float-end" src="static/img/${SEMIC2.value}.svg" width="25">`;
            document.getElementById("PS1").value = SEMIC2.value;
        const t1 = pais.value;
        if(t1){
            document.getElementById("PS1").disabled = false;
        }
        }
        else{
            document.getElementById("LPS1").innerHTML = `${SEMIC1.value} <img class="float-end" src="static/img/${SEMIC1.value}.svg" width="25">`;
            document.getElementById("PS1").value = SEMIC1.value;
            const t2 = pais.value;
        if(t2){
            document.getElementById("PS1").disabled = false;
        }
        }
    }
    if(pais.id == "SEMIC3" || pais.id == "SEMIC4"){
        document.getElementById("Lfinal2").innerHTML = `<img class="float-start" src="static/img/${pais.value}.svg" width="25"> ${pais.value}`;
        document.getElementById("final2").value = pais.value;
        const final2 = pais.value;
        if(final2){
            document.getElementById("final2").disabled = false;
        }
        if(pais.value == SEMIC3.value){
            document.getElementById("LPS2").innerHTML = `<img class="float-start" src="static/img/${SEMIC4.value}.svg" width="25"> ${SEMIC4.value}`;
            document.getElementById("PS2").value = SEMIC4.value;
            const f1 = pais.value;
            if(f1){
            document.getElementById("PS2").disabled = false;
        }
        }
        else{
            document.getElementById("LPS2").innerHTML = `<img class="float-start" src="static/img/${SEMIC3.value}.svg" width="25"> ${SEMIC3.value}`;
            document.getElementById("PS2").value = SEMIC3.value;
            const f2 = pais.value;
            if(f2){
            document.getElementById("PS2").disabled = false;
        }
        }
    }
}

function final(id){
    let pais = document.querySelector(id);
    document.getElementById("campeon-elegido").innerHTML = `${pais.value} <img src="static/img/${pais.value}.svg" width="25">`;
    if(pais.value == final1.value){
        document.getElementById("segundo").value = final2.value;
        console.log("SEGUNDO",document.getElementById("segundo").value)
    }
    else{
        document.getElementById("segundo").value = final1.value;
    }

}
function tercer(id){
    let pais = document.querySelector(id);
    if(pais.value == PS1.value){
        document.getElementById("cuarto").value = PS2.value;
    }
    else{
        document.getElementById("cuarto").value = PS1.value;
    }

}
