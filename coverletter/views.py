import os

from django.shortcuts import render
from django_tex.shortcuts import render_to_pdf
from .forms import CoverLetterForm
from langchain.llms import OpenAI

def generate_cover_letter_description(job_description,year_of_experience):
    # Initialize Langchain with OpenAI
    llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Define the prompt
    prompt = ('Generate the body of a job application cover letter based on the following job description, '
              'and a year of experience is "' + str(year_of_experience) + '". '
              'Exclude any salutations or addressing lines such as "Dear Hiring Manager". '
              'Focus on the applicant’s skills and experiences relevant to this job description: "'
              + job_description + '"')
    # Generate the cover letter
    response = llm(prompt)
    return response


def generate_cover_letter(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            job_description = form.cleaned_data['job_description']
            year_of_experience = form.cleaned_data['year_of_experience']
            cover_letter_description = generate_cover_letter_description(job_description,year_of_experience)
            context = {
                **form_data,  
                'cover_letter_description': cover_letter_description,  
            }
            template_name = 'cover_letter_template.tex'
            return render_to_pdf(request, template_name, context, filename='cover.pdf')
    else:
        form = CoverLetterForm()

    return render(request, 'job_description_form.html', {'form': form})


