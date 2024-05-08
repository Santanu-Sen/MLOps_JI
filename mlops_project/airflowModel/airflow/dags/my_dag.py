from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Import the functions from your Python files
from main import main
from speech2text import speech_to_text
from text2speech import text_to_speech
from translation import translate_text

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

# Instantiate the DAG
dag = DAG(
    'translation_pipeline',
    default_args=default_args,
    description='A DAG to orchestrate the translation pipeline tasks',
    schedule_interval=None,  # Run once
)

# Define tasks using PythonOperator

def execute_translation_pipeline():
    # Execute the main function
    main()

with dag:
    # Task to capture speech and convert it to text
    task_speech_to_text = PythonOperator(
        task_id='speech_to_text',
        python_callable=speech_to_text,
    )

    # Task to translate the text to the target language
    task_translate_text = PythonOperator(
        task_id='translate_text',
        python_callable=translate_text,
        op_kwargs={'source_language': 'en', 'target_language': 'hi'},  # Example source and target languages
    )

    # Task to convert translated text to speech in the target language
    task_text_to_speech = PythonOperator(
        task_id='text_to_speech',
        python_callable=text_to_speech,
        op_kwargs={'language': 'hi'},  # Example target language
    )

    # Task to execute the entire translation pipeline
    task_execute_pipeline = PythonOperator(
        task_id='execute_translation_pipeline',
        python_callable=execute_translation_pipeline,
    )

    # Define task dependencies
    task_speech_to_text >> task_translate_text >> task_text_to_speech >> task_execute_pipeline

