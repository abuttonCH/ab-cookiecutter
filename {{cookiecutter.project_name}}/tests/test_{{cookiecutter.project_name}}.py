from {{cookiecutter.project_name}} import __version__

from tests.helper import add_timestamp

from tests.output import TEST_OUTPUT

def test_version():
    assert __version__ == '0.1.0'

def test_file():
    # create timestamped output filename
    output_filename = add_timestamp(f"{TEST_OUTPUT}/test.txt")
    # write output file to the test_output directory
    open(output_filename,"w+") as f:
        f.write("example")
