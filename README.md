    Tests connection to an IMAP server using SSL/TLS.
    
    Args:
        server (str): IMAP server hostname (e.g., imap.gmail.com)
        username (str): IMAP username
        password (str): IMAP password
        port (int): IMAP SSL port (default: 993)
    
    Returns:
        bool: True if connection and login successful, False otherwise
    """
