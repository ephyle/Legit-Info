#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cfc_app/tests.py -- Perform simple tests
Written by James Stewart and Tony Pearson, IBM, 2020
Licensed under Apache 2.0, see LICENSE for details
"""

# System imports
# Django and other third-party imports
import os
from unittest import mock

from django.test import Client
from django.core.management import call_command
from django.test import TestCase
from io import StringIO

# Application imports

client = Client()


class GetDatasetsCustomCommandtests(TestCase):
    @mock.patch.dict(os.environ, {"FOB_STORAGE": "/tmp/"})
    @mock.patch('cfc_app.legiscan_api.LegiscanAPI.get_datasetlist', return_value='{"status":"OK","datasetlist":[{"state_id":26,"session_id":1748,"year_start":2021,"year_end":2021,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2021 Regular Session","session_name":"2021 Regular Session","dataset_date":"2021-12-31","dataset_hash":"1ed379b4dd09328b21e5842ed3887f08","dataset_size":6074816,"access_key":"4EWZIj13Aq5ZblsrKe2WnL"},{"state_id":26,"session_id":1616,"year_start":2019,"year_end":2019,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2019 Regular Session","session_name":"2019 Regular Session","dataset_date":"2021-12-31","dataset_hash":"758271e29ef101e2acbbee4deeb58ef9","dataset_size":5617521,"access_key":"5LYnWXTQXlZQaPJpavqziU"},{"state_id":26,"session_id":1515,"year_start":2017,"year_end":2017,"prefile":0,"sine_die":1,"prior":1,"special":1,"session_tag":"1st Special Session","session_title":"2017 1st Special Session","session_name":"2017 1st Special Session","dataset_date":"2021-12-31","dataset_hash":"ac42d27b8508cd896b109dcc886f4250","dataset_size":159109,"access_key":"5tS6HLKFPzlOR5UVOaUGOk"},{"state_id":26,"session_id":1224,"year_start":2017,"year_end":2017,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2017 Regular Session","session_name":"2017 Regular Session","dataset_date":"2021-12-31","dataset_hash":"8e96118260969d33a2ca4901ddbc6b16","dataset_size":5132347,"access_key":"Uu2nIH0HV8feb4Ty0GKnD"},{"state_id":26,"session_id":1138,"year_start":2015,"year_end":2015,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2015 Regular Session","session_name":"2015 Regular Session","dataset_date":"2021-12-31","dataset_hash":"bc02a990e5572c5f5db6fec6c9498eab","dataset_size":5069664,"access_key":"3XlA78OO4nElKKmNm7jdfu"},{"state_id":26,"session_id":977,"year_start":2013,"year_end":2013,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2013 Regular Session","session_name":"2013 Regular Session","dataset_date":"2021-12-31","dataset_hash":"16254428bdfbd6331505e4df771e44d2","dataset_size":4301530,"access_key":"6UoW57rNyuiYU1bl6ww8Tf"},{"state_id":26,"session_id":85,"year_start":2011,"year_end":2011,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2011 Regular Session","session_name":"2011 Regular Session","dataset_date":"2021-12-31","dataset_hash":"a522cc9428c81f79dbe5e09d0f92c436","dataset_size":4352754,"access_key":"5onw8XXavRHI3dkKQTmW5s"},{"state_id":26,"session_id":56,"year_start":2009,"year_end":2009,"prefile":0,"sine_die":1,"prior":1,"special":0,"session_tag":"Regular Session","session_title":"2009 Regular Session","session_name":"2009 Regular Session","dataset_date":"2021-12-31","dataset_hash":"e493fce95901b10fd2bb3e3c1b9812d2","dataset_size":2165076,"access_key":"5VP5NrQxT7DALXMlSby7AB"}]}')
    def test_analyze_text(self, mock_get_datasetlist):
        out = StringIO()
        call_command('analyze_text', '--api', '--frequency', '1', stdout=out)

        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '{"status": "UP"}')

# add_arguments
    def add_arguments(self):
        # Verify that we get the expected arguments with the proper types
        return

# process_state
	def process_state_with_bill_ID_in_header(self):
		#verfiy that with a bill ID in the header it processes the legislation
		return
	def process_state_without_bill_ID_in_header(self):
		#verfiy that with no bill ID in the header the file name is removed
		return

# process_legislation
	def process_legislation_with_laws_not_none_and_zero(self):
		return

#relevance_nlu
	def relevance_nlu_with_text_returns_concept(self):
		return

#format_rel
	def format_rel_with_second_element_unknown(self):
		return

	def format_rel_with_second_element_known(self):
		return