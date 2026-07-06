async function translateText(){

let formData=new FormData()

formData.append(
"text",
inputText.value
)

formData.append(
"source",
source.value
)

formData.append(
"target",
target.value
)

let response=
await fetch(
"/translate",
{
method:"POST",
body:formData
}
)

let data=
await response.json()

outputText.value=
data.translated

detected.innerHTML=
data.detected

}


function copyText(){

navigator.clipboard.writeText(
outputText.value
)

alert("Copied")

}


async function speakText(){

let formData=
new FormData()

formData.append(
"text",
outputText.value
)

let response=
await fetch(
"/speak",
{
method:"POST",
body:formData
}
)

let data=
await response.json()

audioPlayer.src=
data.audio+"?"+new Date().getTime()

audioPlayer.play()

}


function swap(){

let temp=source.value
source.value=target.value
target.value=temp

}


function darkMode(){

document.body.classList.toggle(
"dark"
)

}


async function showHistory(){

let response=
await fetch("/history")

let data=
await response.json()

let html=""

data.forEach(x=>{

html+=`

<p>

${x.original}

➡

${x.translated}

</p>

`

})

history.innerHTML=html

}


function voiceInput(){

const recognition =
new webkitSpeechRecognition()

recognition.lang='en-US'

recognition.start()

recognition.onresult=function(event){

inputText.value=
event.results[0][0].transcript

}

}