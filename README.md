  
**This is totally unofficial version of invokeai which can be used with Intel Arc GPU.**

- It's based on InvokeAI 6.12.0 and was modified with AI to make it work with torch-xpu.
- It's provided as it is. I have no plans to commit it to main invokeai repository.
- Tested with Intel Arc Pro B50 GPU at Windows 11 and Bazzite Linux

**Installation**

Installation use manual method explained at original invokeai repository with some modifications. Read original instructions from here: <a href="https://invoke-ai.github.io/InvokeAI/installation/manual/">https://invoke-ai.github.io/InvokeAI/installation/manual/</a>

Follow original instructions except for step 8.

 <code>uv pip install {location of your local invokeai_intelGPU repository} --python 3.12 --python-preference only-managed --force-reinstall --torch-backend=xpu</code>

**My configuration file - invokeai.yaml**

<code>device: "xpu:0"
host: 0.0.0.0
port: 9090</code>


 
