---
created: 2024-01-17-Wednesday 16:35
modified: 2024-10-03-Thursday 13:52
publish: 
---

#### Sigmon

sigmonctl stream --channels /Motif/TrackerState
sigmonctl list

Dump raw logged streams:
log stream --debug --info --predicate "process='MotifTools'"
log stream --debug --info --predicate "process='peopleawarenessd'"
log stream --debug --info --predicate 'subsystem="com.apple.AttentionLLM"'
log stream --debug --info --predicate 'subsystem="com.apple.TrackerStateBridge"'

Check the permissions on the device:
login -f mobile defaults read com.apple.motif

Command to enable permissions:
login -f mobile defaults write com.apple.motif AudioDetectorEnabled -bool YES

To start streaming to sunscreen
sigmonctl serve start
pkill -9 sigmond

Motif script to run on device - [[set_live.sh]]
[[set_clean_install.sh]]

Launch Sunglasses to visualize Motif tracks:
LaunchApp com.apple.internal.SunGlasses

### LLM

python client/ws_client.py --host sc0102a-dhcp194.apple.com --port 1337 --prompt 'how many planets are there' --temp 0.5 --backend llama.cpp --top-p 0.5

Command to run the Mixtral model for attention on server
./server -m models/Mixtral-8x7B-Instruct-v0.1-GGUF/mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf --host 0.0.0.0 -t 24 -c 0 --mlock

### Root creation

Stored somewhere here: ~/Library/Developer/Xcode/DerivedData/Motif-csydtojxmigbumbrsutgqatdvdam/Build/Intermediates.noindex/InstallIntermediates/appletvos
 
ditto -cz InstallableProducts /Volumes/Project/tmp/Motif-All-appletvos-Root.cpgz

scp /Volumes/Project/tmp/Motif-All-appletvos-Root.cpgz root@b:/var/mobile/Motif-All-appletvos-Root.cpgz

snapshottool golive 2

darwinup install Motif-All-appletvos-Root.cpgz

launchctl unload /System/Library/LaunchDaemons/com.apple.peopleawarenessd.plist
launchctl load /System/Library/LaunchDaemons/com.apple.peopleawarenessd.plist

Script from Paul: [[make_motif_root.sh]]

### Device

 Command to install HomeDiagnostic: `knox home-diag SapphirePalazzo` (confluence [link](https://confluence.sd.apple.com/display/COREPLATFORM/Install+HomeDiagnostics))

From Kyle on defanging system when running into codesigning errors when building the app (on mac):
sudo defaults write /Library/Preferences/com.apple.security.coderequirements Entitlements -string always;

From Manuel - boot args when running into codesigning errors
nvram boot-args="cs_enforcement_disable=1 amfi=-1 launchctl_enforce_codesign=0 debug=0x14e amfi_allow_any_signature=1 amfi_unrestrict_task_for_pid=1 disable_exc_resource_during_audio=0"

If you see errors about device having a read only partition or APFS errs, run:
snapshottool golive 2; reboot

Command to connect device to a network: `mobilewifitool -- join -i en0 --ssid=ABeautifulPlace --password=WaffleIr0n ; mobilewifitool -- autojoin add --ssid=ABeautifulPlace`

sysctl -a : to get device hardware details

swift-format format -i --configuration configuration.swift-format AttentionKit/LLMSupport/*.swift

For debugging on screen: sunboardctl debugging overlay --toggle

#### Bypass setup screen - skip onboarding

login -f mobile defaults write com.apple.purplebuddy SetupDone -bool YES;
login -f mobile defaults write com.apple.purplebuddy ForceNoBuddy -bool YES;
snapshottool golive 2;
mobilewifitool -- join -i en0 --ssid=ABeautifulPlace --password=WaffleIr0n ;
mobilewifitool -- autojoin add --ssid=ABeautifulPlace;
reboot

#### Setup instructions from Manuel

```
nvram PebbleMode=2
login -f mobile defaults write com.apple.purplebuddy SetupDone -bool YES
login -f mobile defaults write com.apple.purplebuddy ForceNoBuddy -bool YES
jetsam_properties set-framework-roots true
assistant_tool enableAssistant
assistant_tool siriDataSharingOptInStatus --set false
assistant_tool suppressSiriDataSharingOptInAlert --set true
corespeech_tool disableVoiceTrigger #enableVoiceTrigger
mobilewifitool -- join -i en0 --ssid=ABeautifulPlace --password=WaffleIr0n ; mobilewifitool -- autojoin add --ssid=ABeautifulPlace
login -f mobile defaults write com.apple.frontboardservices.device_emulation PBDebugControlsHeight -float 100
lockdown_query set NULL DeviceName ‘MyDevice’
jetsam_properties set Extension Override com.apple.sigmon.diagnostic MemoryLimit -1
casperctl debugging overlay --toggle
ffctl CharacterInteractionKit/enableMotifDictation=on
snapshottool golive 2
reboot
```

#### Restore Device

[Instruction to DFU](https://confluence.sd.apple.com/pages/viewpage.action?spaceKey=ApplicationTechnologies&title=How+to+DFU) from Zi Qian

From Sylvain:
Reboot: astrisctl reset
DFU: astrisctl relay dfu 1

### Lotus
#### Wireless SSH wifi

On device create /var/root/.ssh/authorized_keys or ~/.ssh/authorized_keys
Copy your id_rsa.pub in it echo "ssh-rsa AAAAB..." >> /var/root/.ssh/authorized_keys
Turn on SSH : cuutil ssh on
Device & Remote need to be on same wifi eg: ABeautifulPlace
Get ip address of device: ifconfig | grep 192 or grep 17
If you get a man in the middle attack warning go to your machine's ~/.ssh/known_hosts and remove the keys for the ip address you want to ssh to

### Llama.cpp

setting up llama.cpp server: `./server -m models/dolphin-2.7-mixtral-8x7b/dolphin-2.7-mixtral-8x7b.Q5_K_M.gguf --host 0.0.0.0`
server call instead of the regular main binary

``` 
curl --request POST \
     --url http://sc0102a-dhcp194.apple.com:8080/completion \
     --header "Content-Type: application/json" \
     --data "$(jq -nc --arg prompt "$ATTNPROMPT" --arg grammar "$ATTNGRAMMAR" '{prompt: $prompt, grammar: $grammar, n_predict: 128, cache_prompt: true}')" \
     -w "\nTotal time: %{time_total} seconds\n"
```

here is the file that sets the right env variables to test it: ![[attn-prompt.sh]]
Quick command to query the attention llm server

``` 
curl --request POST \
     --url http://17.220.23.58:1234/completion \
     --header "Content-Type: application/json" \
     --data "$(jq -nc --arg prompt "$ATTNPROMPT" '{prompt: "hello, hows it going with you?", n_predict: 128}')" \
     -w "\nTotal time: %{time_total} seconds\n"

```
### Turi Bolt

Run this config file to launch a Turi job - `bolt task submit --interactive` from the directory where the config file is. Need to be in this conda env: `conda activate /Users/ammarh/anaconda3/envs/turi`
![[config.yaml]]
**Python Notebooks:**
![[turi-assetstore.ipynb]]

![[turi-ML.ipynb]]

[Bolt](https://bolt.apple.com/docs/task-basics.html) & [Hub](https://turihub.apple.com/docs/workflows/quickstart/getting-started/) docs; Tasks [dashboard](https://bolt.apple.com/tasks)

bolt task submit --interactive --tar .

To start a task from the current directory: `bolt task submit --config onshot-train-config.yaml --tar .`

bolt task scp -r h6sawxyhrb:/mnt/task_runtime/TinyLlamaAttentionFinetuned/ ~/j595/EmbodiedReasoning/Attention/TinyLlamaAttentionFinetuned10k/.
bolt task ssh 7gwu992zs7
bolt task sync 7gwu992zs7 --local-dir .
bolt task viewport h6sawxyhrb 8888
bolt task copy_artifacts h6sawxyhrb --dest tmp/
bolt task show <task_id>
In order to get tmux on turi:
apt install software-properties-common; add-apt-repository main; apt update; apt install tmux

**Download artifacts from bolt using S3** - [steps](https://bolt.apple.com/docs/artifacts.html#through-other-s3-tools)
``` 
eval `bolt task get-credentials rgmcrpfmnc`
aws --endpoint-url https://conductor.data.apple.com s3 --no-verify-ssl cp --recursive s3://bolt-prod-973545915/tasks/rgmcrpfmnc/output/ .
```

**Copy artifacts from bolt on to S3**
``` 
find edu_fineweb10B -name "*.npy" -exec sh -c 'aws --endpoint-url https://conductor.data.apple.com s3 cp {} "$BOLT_TASK_OUTPUT_PATH/edu_fineweb10B/$(basename {})"' \;
```

**Setting up Conductor**
curl --proto '=https' --tlsv1.2 -sSf https://pages.github.pie.apple.com/storage-orchestration/conductor/docs/setup-conductor.sh -o setup-conductor.sh
chmod +x setup-conductor.sh
bash setup-conductor.sh

conductor s3api create-bucket --bucket fc3-attention-finetuning

### Docker

Have a Dockerfile in the directory, start the Docker application and then run:

```
docker images - lists all existing images
docker build . -t attnimage
docker ps - list running container
docker cp <file> container_id:/<path> : container_id is what is running and not the image id/ tag (ie attnimage)
docker run -it attnimage - creates a new container from the attnimage
```

**To push docker images to the apple registry** - first tag it with the url and then upload
docker tag attnimage docker.apple.com/ammar_husain/prod/attnimage
docker push docker.apple.com/ammar_husain/prod/attnimage

Need to run to get the conda env loaded
. /etc/profile.d/conda.sh && conda activate myen

### Persona Identifier

To update persona identifiers in SunCore on device (from Anton) - this enables you to use personaClient:
sunctl insertPersona identifier=1234 firstName=joe lastName=shmoe
ammar = 87FC2933-80D2-471E-A131-DEF48EE36090
madison = 81CFE414-30CD-44C9-8594-59A04B78B5C0
bob = 1A4D493B-B117-4158-8B24-E14F9B4CF1A4 (poster)

``` 
sunctl insertPersona identifier=7218FE20-0542-2443-9963-A2A199B4C665 firstName=ada
sunctl insertPersona identifier=B20C96B8-294A-FC67-954C-BB94443A7292 firstName=kendra
sunctl insertPersona identifier=640F82A8-E34F-A8EF-BC65-3081A3BD3AC1 firstName=hudson
sunctl insertPersona identifier=1E6AA2B7-4741-63B9-333D-EEA6ABF6DC80 firstName=sadhil
sunctl insertPersona identifier=E768D35D-CB4A-F695-946B-BBB3718AEEEA firstName=wallace
sunctl insertPersona identifier=7E5F5095-BD40-9102-6B0C-6BAABA30214D firstName=jesse
```
### Build SDK versions

[BuildWatch](https://buildwatch.apple.com/?projects=AttentionKit&trains=SapphirePalazzo)
Check what SDK version made it into which build:
xbsfind projectversions --update CurrentSapphirePalazzo AttentionKit

### Run isSpeaking model from Josh T instead of NatVoc
``` 
login -f mobile defaults write com.apple.motif FaceProcessingPerSecond -int 10 
login -f mobile defaults write com.apple.motif NatVocEnabled -bool false 
login -f mobile defaults write com.apple.motif ComputeFaceLandmarks -bool true 
login -f mobile defaults write com.apple.motif VNTracker -bool true
```

### Disable AmbientExperience

Footgun approach suggested by August

```
mv /System/Library/ExtensionKit/Extensions/AmbientExperience.appex /System/Library/ExtensionKit/Extensions/AmbientExperience-foo.appex
pkill -9 AmbientExperience
```

### WorldStateCollator debugging
``` 
amemctl
getAllWorldStateSnapshots
```

``` 
jetsam_properties set --force Daemon SCOPE:com.apple.agentmemoryd MemoryLimit -1
reboot
```

launchctl kickstart system/com.apple.agentmemory

### Llama3 hosted superserver
``` 
curl -vvv -X 'POST' \
 'https://superserver.corp.apple.com:9124/completion' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{"cache_prompt":true, "stream":false,"n_predict":500,"prompt":"<|start_header_id|>system<|end_header_id|>\nHI! You are a friendly robot that talks like a pirate. The current time is 2024-08-13 11:15:18.811000<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\nHi, how are you?<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>\nDoing great.<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\nCan tell me the current time?<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>\nThe current time is 10:15<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\nAre you sure?<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>"}'
```

### AttentionLLM server
``` 
curl --request POST \
     --url http://j595-attention.corp.apple.com:1234/completion \
     --header "Content-Type: application/json" \
     --data "$(jq -nc --arg prompt "$ATTNPROMPT" '{prompt: "hello, hows it going with you?", n_predict: 128}')" \
     -w "\nTotal time: %{time_total} seconds\n"
```

To run the model on local@j595-attention.corp.apple.com:
``` 
./llama-server -m /Users/local/j595/EmbodiedReasoning/Attention/FinetunedModels/f-SmolLM-360M-Instruct-2024-08-09_15-13-07-synth-30k-with-medium-engagement-with-punctuation-largecorpus-ordered-entities.json.gguf --host 0.0.0.0 -t 24 -c 0 --mlock --port 0987
```

### Code submission
[Instructions](https://quip-apple.com/Dvc2AbCDGo3G)
Steps:
``` 
sudo xbs buildit -project AttentionKit -release SapphirePalazzo AttentionKit # from ~/j595 
git tag AttentionKit-24.1; git push origin AttentionKit-24.1
git log AttentionKit-24..AttentionKit-24.1 | grep 'rdar' # fetch radars that were fixed
xbs submitproject -git -url https://github.pie.apple.com/heavenly/AttentionKit -tag AttentionKit-24.1 SapphirePalazzo

```

### YOLO model
`pip install -U ultralytics`
`yolo detect track model=yolo11l-homework-best.pt source=0 show=true conf=0.7`


### Bubbles server
REACT_APP_LOCAL_RELAY_SERVER_URL=[wss://superserver.corp.apple.com:1339/v1/realtime](wss://superserver.corp.apple.com:1339/v1/realtime) npm start

### Glide
From Dmitry:
(s:conversationagent && m:transcript)