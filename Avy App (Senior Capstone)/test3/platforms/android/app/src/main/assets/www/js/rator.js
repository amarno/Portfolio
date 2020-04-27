/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var app = {
    // Application Constructor
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);

    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    onDeviceReady: function() {
        this.receivedEvent('deviceready');
    },

    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};

app.initialize();

//rating variables

var cl; //critical loading
var cw; //critical warming 
var last; //other variables 

// button variables 

var clnb = document.getElementById("cln"); //no critical loading button 
var clyb = document.getElementById("cly"); //yes critical loading 
var cwnb = document.getElementById("cwn"); //... 
var cwyb = document.getElementById("cwy");
var lyb = document.getElementById("lastyes");
var lnb = document.getElementById("lastno");

//var restart = document.getElementById("top");
var sub = document.getElementById("submit");

//rating functions

if(clnb){
    clnb.addEventListener("click", cln);
    function cln(){
        cl = false;
        clnb.style.backgroundColor = "#AFF8DB";
        clyb.style.backgroundColor = "rgba(255, 255, 255, 0.63";
        document.getElementById("cw").style.display="block";
        document.getElementById("cw").scrollIntoView(true);
        localStorage.setItem('rating', 'MODERATE');
    };
};

if(clyb){
    clyb.addEventListener("click", cly);
    function cly(){
        cl = true;
        clyb.style.backgroundColor = "#FFBEBC";
        clnb.style.backgroundColor = "rgba(255, 255, 255, 0.63";
        document.getElementById("cw").style.display="block";
        document.getElementById("cw").scrollIntoView();
        localStorage.setItem('rating', 'HIGH');
    };
};

if(cwnb){
    cwnb.addEventListener("click", cwn);
    function cwn(){
        cw = false;
        cwnb.style.backgroundColor = "#AFF8DB";
        cwyb.style.backgroundColor = "rgba(255, 255, 255, 0.63";
        document.getElementById("last").style.display="block";
        document.getElementById("last").scrollIntoView();
        if(cl==false){
            localStorage.setItem('rating', 'MODERATE');
        };

    };
};

if(cwyb){
    cwyb.addEventListener("click", cwy);
    function cwy(){
        cw = true;
        cwyb.style.backgroundColor = "#FFBEBC";
        cwnb.style.backgroundColor = "rgba(255, 255, 255, 0.63";
        document.getElementById("last").style.display="block";
        document.getElementById("last").scrollIntoView();
        localStorage.setItem('rating', 'HIGH');

    };
};

if(lyb){
    lyb.addEventListener("click", lastyes);
    function lastyes(){
        last = true;
        lyb.style.backgroundColor = "#FFBEBC";
        lnb.style.backgroundColor = "rgba(255, 255, 255, 0.63";
        document.getElementById("final").style.display="block";
        document.getElementById("final").scrollIntoView();
        if(cl==false & cw==false){
            localStorage.setItem('rating', 'CONSIDERABLE');
        };
    };
};

if(lnb){
    lnb.addEventListener("click", lastno);
    
    function lastno(){
        last = false;
        lnb.style.backgroundColor = "#AFF8DB";
        lyb.style.backgroundColor = " rgba(255, 255, 255, 0.63";
        document.getElementById("final").style.display="block";
        document.getElementById("final").scrollIntoView();

    };
};

if(sub){
    console.log("helloo");
    sub.addEventListener("click", submit);

    function submit(){
        window.location = "answer.html";
    };
};


// alerts for more information questions 

var clc = document.getElementById("clq");
var cwc = document.getElementById("cwq");
var rlc = document.getElementById("rlq");
var rac = document.getElementById("raq");
var wlc = document.getElementById("wlq");

if(clc){
    clc.addEventListener("click", clq);
    function clq(){
            var message = "Add the total snowfall from the past 24 hours AND the predicted snowfall for the day. If it is 30cm/12in or more there is critical loading";
            var title = "Critical Loading";
            var buttonName = "Got it";
            navigator.notification.alert(message, alertCallback, title, buttonName);
            
            function alertCallback() {
               console.log("Alert is Dismissed!");
            };
    };
};

if(cwc){
    cwc.addEventListener("click", cwq);
    function cwq(){
        var message = "Warming temperatures can create a warm heavy layer on top of the snowpack and is likely to cause instablity";
            var title = "Critical Warming";
            var buttonName = "Got it";
            navigator.notification.alert(message, alertCallback, title, buttonName);

            function alertCallback() {
                console.log("Alert is Dismissed!");
             };
    };
};

if(rlc){
    rlc.addEventListener("click", rlq);
    function rlq(){
        var message = "If there has been 30cm/12in or more snow fall or significant wind depositing in the last 48 hours there is recent loading";
        var title = "Recent Loading";
        var buttonName = "Got it";
        navigator.notification.alert(message, alertCallback, title, buttonName);

        function alertCallback() {
            console.log("Alert is Dismissed!");
         };
    };
};

if(rac){
    rac.addEventListener("click", raq);
    function raq(){
        var message = "Look around, ask around. Have there been avalanches recently? If you do not know, answer yes";
        var title = "Recent Slides";
        var buttonName = "Got it";
        navigator.notification.alert(message, alertCallback, title, buttonName);

        function alertCallback() {
            console.log("Alert is Dismissed!");
         };
    };
};

if(wlc){
    wlc.addEventListener("click", wlq);
    function wlq(){
        var message = "Ask around and dig in the snow. If you do not know, answer yes. Persistant weak layers can be buried deep in the snow pack and difficult to identify. They are also the cause of many large avalanches";
        var title = "Persistant Weak Layer";
        var buttonName = "Got it";
        navigator.notification.alert(message, alertCallback, title, buttonName);

        function alertCallback() {
            console.log("Alert is Dismissed!");
         }; 
    };

};

// answer page functions

function answer(){
    console.log(localStorage.getItem('rating'));

    var answer = document.getElementById("answer"); 
    var rate = localStorage.getItem('rating');

    if(answer){
        document.getElementById("answer").innerHTML = rate;
    };

    if(rate == "HIGH"){ 
        document.getElementById("high").style.display = "block";

    };
    
    if(rate=="CONSIDERABLE"){
        document.getElementById("con").style.display = "block";
    };

    if(rate=="MODERATE"){
        document.getElementById("mod").style.display = "block";
    };

};

//page directs 

var main = document.getElementById("home"); 

if(main){
    main.addEventListener("click", mainMenu)

    function mainMenu(){
        window.location="index.html"
    };

};

var beacon = document.getElementById("beacon");

if(beacon){
    console.log("beacon check");
    beacon.addEventListener("click", goToBeacon);

    function goToBeacon(){
        window.location = "beaconCheck.html";
    };
};

