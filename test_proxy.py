import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import json
from starlette.testclient import TestClient

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app

class TestProxyRequest(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
    @patch('app.get')
    def test_proxy_request_success(self, mock_get):
        # Mock the response from checkip.amazonaws.com
        mock_response = MagicMock()
        mock_response.text = "192.0.2.1\n"
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Set environment variables for proxy
        os.environ['HTTP_PROXY'] = 'http://proxy.example.com:8080'
        os.environ['HTTPS_PROXY'] = 'http://proxy.example.com:8080'
        
        # Make request to our endpoint
        response = self.client.get('/proxy')
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check that the content contains the expected IP
        self.assertIn('192.0.2.1', response.text)
        
        # Check that the proxy settings were used
        self.assertIn('http://proxy.example.com:8080', response.text)
        
        # Verify that the get function was called with the correct parameters
        mock_get.assert_called_once_with(
            'https://checkip.amazonaws.com/',
            proxies={
                'http': 'http://proxy.example.com:8080',
                'https': 'http://proxy.example.com:8080'
            },
            timeout=10
        )
    
    @patch('app.get')
    def test_proxy_request_error(self, mock_get):
        # Mock an error response
        mock_get.side_effect = Exception("Connection error")
        
        # Make request to our endpoint
        response = self.client.get('/proxy')
        
        # Check that the response has error status code
        self.assertEqual(response.status_code, 500)
        
        # Check that the error message is in the response
        self.assertIn('Connection error', response.text)

if __name__ == '__main__':
    unittest.main()