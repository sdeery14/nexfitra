import pytest
from airflow.models import DagBag

# Define a fixture that loads the DAGs from the DAGs directory
@pytest.fixture
def dagbag():
    return DagBag(dag_folder="dags", include_examples=False)

# Define a test function that tests the 'example_dag' DAG
def test_example_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="example_dag")
    assert dag is not None
    assert len(dag.tasks) == 1
    assert 'start' in [task.task_id for task in dag.tasks]
