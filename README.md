  
**This is totally unofficial version of invokeai which can be used with Intel Arc GPU.**

- It's based on InvokeAI 6.12.0 which was modified with AI to make it work with Intel Arc GPU at Windows 11
- It's provided as it is. I have no plans to commit it to main invokeai repository.
- Installation tested with Intel Arc Pro B50 GPU at Windows 11. Propably works with Linux too.

**Installation**

Tools needed for installation:
- python 3.12  
- git  
- uv
- pnpm 

You can install all these tools using following command:

<code> winget install Python.Python.3.12 Git.Git  GitHub.GitLFS astral-sh.uv  pnpm.pnpm</code>

Installation use manual method explained at original invokeai repository with some modifications. Read original instructions from here: <a href="https://invoke-ai.github.io/InvokeAI/installation/manual/">https://invoke-ai.github.io/InvokeAI/installation/manual/</a>

Here are commands to make installation at Windows 11 commandline:

<code>
git clone https://github.com/ilmarille2/InvokeAI_intelGPU
mkdir InvokeA
cd .\InvokeAI\
uv venv --relocatable --prompt invoke --python 3.12 --python-preference only-managed .venv
.venv\Scripts\activate  
cd ..\InvokeAI_intelGPU\invokeai\frontend\web\ 
pnpm i
pnpm build
cd ..\..\..\..\InvokeAI\
uv pip install ..\InvokeAI_intelGPU --python 3.12 --python-preference only-managed --force-reinstall --torch-backend=xpu
deactivate
.venv\Scripts\activate
invokeai-web --root .</code>

If you want you can add to invokeai.yaml configuration file setting **device: "xpu:0"**

**Related projects**

- <a href="https://github.com/Raasu2/invokeai-xpu">https://github.com/Raasu2/invokeai-xpu</a>


 
