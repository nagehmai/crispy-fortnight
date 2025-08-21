import imaplib
import argparse
import sys
import ssl

def test_imap_connection(server, username, password, port=993):
    """
    Test connection to an IMAP server using SSL/TLS.
    
    Args:
        server (str): IMAP server hostname (e.g., imap.gmail.com)
        username (str): IMAP username
        password (str): IMAP password
        port (int): IMAP SSL port (default: 993)
    
    Returns:
        bool: True if connection and login successful, False otherwise
    """
    try:
        # Create an IMAP4_SSL object to connect using SSL/TLS
        context = ssl.create_default_context()
        imap = imaplib.IMAP4_SSL(server, port, ssl_context=context)
        
        # Attempt to log in
        imap.login(username, password)
        
        # Select the inbox to verify access
        status, _ = imap.select('INBOX')
        if status != 'OK':
            print(f"Error: Unable to select INBOX: {status}")
            return False
        
        print(f"Successfully connected to {server} and logged in as {username}")
        imap.logout()
        return True
        
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {str(e)}")
        return False
    except Exception as e:
        print(f"Connection error: {str(e)}")
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test IMAP server connection using SSL/TLS")
    parser.add_argument('--server', required=True, help="IMAP server hostname (e.g., imap.gmail.com)")
    parser.add_argument('--username', required=True, help="IMAP username")
    parser.add_argument('--password', required=True, help="IMAP password")
    
    args = parser.parse_args()
    
    # Test the IMAP connection
    success = test_imap_connection(args.server, args.username, args.password)
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
