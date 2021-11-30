# import ordering
# import pytest
#
# @pytest.mark.run(order=2)
# def test_foo():
#     print("用例11111111111")
#     assert True
#
# @pytest.mark.run(order=1)
# def test_bar():
#     print("用例22222222222")
#     assert True
#
# @pytest.mark.run(order=3)
# def test_g():
#     print("用例333333333333333")
#     assert True
import sys, os

from contextlib import ExitStack

profileList = {}

def PropValue(envfile):

    with open(envfile) as profile:

        new_profile = profile.readlines()

        # print(new_profile)

    for line in new_profile:

        line_key = line.strip().split(":", 1)[0]

        profileList[line_key] = line.strip().split(":", 1)[1]
        print(line_key)

    print(profileList)
def EnvReplaceYaml(yamlfile, newyamlfile):

    try:

        with ExitStack() as stack:

            yml_file = stack.enter_context(open(yamlfile,'r+'))

            yml_output = stack.enter_context(open(newyamlfile,'w'))

            yml_file_lines = yml_file.readlines()

        for line in yml_file_lines:

            new_line = line

            if (new_line.find('') > 0):

                env_list = new_line.split(':')

                env_name = env_list[0].strip()

                replacement = ""

                if env_name in profileList.keys():

                    replacement = profileList[env_name]

                    new_line = new_line.replace('', replacement)

                    yml_output.write(new_line)

    except IOError as e:

        print("Error: " + format(str(e)))

        # raise

if __name__ == "__main__":

    PropValue('./temp.yaml')

    EnvReplaceYaml('./temp.yaml', 'newtemap.yaml')

# temp.yaml

# ---
#
# applications:
#
# - name: --
# memory: 2048m
#
# instances: 1
#
# disk_quota: 2048m
