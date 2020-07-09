# -*- coding: utf-8 -*-

# Copyright (c) IBM Corporation 2019, 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division)
__metaclass__ = type

from ansible_collections.ibm.ibm_zos_ims.plugins.module_utils.IMSDbrc import IMSDbrc  # pylint: disable=import-error
import pytest


test_data_IMSDbrc_extract_values = [
    ('NUMBER OF REGISTERED DATABASES =        0', {'NUMBER OF REGISTERED DATABASES': '0'}),
    ('TIMEZIN = %SYS', {'TIMEZIN': '%SYS'}),
    ('COMMAND AUTH=NONE  HLQ=**NULL**  RCNQUAL=**NULL**', {'COMMAND AUTH': None, 'HLQ': None, "RCNQUAL": None}),
    ('LIST DLOG=NO                 CA/IC/LOG DATA SETS CATALOGED=YES', {'LIST DLOG': False, 'CA/IC/LOG DATA SETS CATALOGED': True}),
    ('LOG RETENTION PERIOD=00.001 00:00:00.0', {'LOG RETENTION PERIOD':'00.001 00:00:00.0'}),
    ('TAPE UNIT=          DASD UNIT=SYSALLDA  TRACEOFF   SSID=IMS1', {'TAPE UNIT': None, 'DASD UNIT': 'SYSALLDA', "SSID": "IMS1"})
]
@pytest.mark.parametrize("line_input, expected_output_dict", test_data_IMSDbrc_extract_values)
def test_IMSDbrc_extract_values(zos_import_mocker, line_input, expected_output_dict):
    # mocker, importer = zos_import_mocker
    imsdbrc = IMSDbrc("SAMPLE COMMAND", "SAMPLE STEPLIB", dynalloc="SAMPLE DYNALLOC")
    actual_output = imsdbrc._extract_values(line_input)
    assert len(actual_output) == len(expected_output_dict)
    print(actual_output)
    for key, val in expected_output_dict.items():
        assert actual_output[key] == val

