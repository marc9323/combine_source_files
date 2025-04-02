# combine_source_files
<br/>
It would be foolish to rely solely on large language models to develop your software.  However, these models are getting sharper by the day.
Most developers will occasionally lack a second set of eyes and would like some LLM to take a look at their code.  
<br/>
However, many models won't accept direct file uploads.  The workaround here is crude but effective:  use a script like this to concatenate every 
code file in your project.  
<br/>
Set the directory containing your code, hit 'Generate', and you'll have a single file, ready to feed the beast.
