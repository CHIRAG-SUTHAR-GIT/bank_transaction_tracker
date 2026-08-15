# Security Policy

## Reporting Security Issues

**Do not open public issues for security vulnerabilities.**

If you discover a security vulnerability in Account Summary Control Room, please email us at **chirag.helpline16@example.com** with:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

Please include "[SECURITY]" in the subject line.

We will:
- Acknowledge receipt within 48 hours
- Provide an initial assessment within 5 business days
- Work with you to understand and fix the issue
- Credit you for the discovery (if desired)

## Security Best Practices

When using Account Summary Control Room:

### Data Protection
- ✅ Keep sensitive data encrypted at rest
- ✅ Use HTTPS in production environments
- ✅ Restrict database file access permissions
- ✅ Store credentials in environment variables or secure vaults
- ✅ Never commit sensitive data to the repository

### Access Control
- ✅ Use strong passwords for web interface
- ✅ Implement user authentication in production
- ✅ Restrict file uploads to authorized users
- ✅ Monitor and audit access logs
- ✅ Use role-based access control

### Secure Deployment
- ✅ Run behind a reverse proxy (nginx, Apache)
- ✅ Use HTTPS with valid certificates
- ✅ Keep dependencies updated
- ✅ Enable Flask debug mode only in development
- ✅ Use environment-specific configurations

### File Handling
- ✅ Validate file uploads (type, size)
- ✅ Scan uploaded files for malware
- ✅ Store uploads outside web root
- ✅ Clean up temporary files
- ✅ Implement file access controls

### Database Security
- ✅ Use strong passwords for database access
- ✅ Limit database user privileges
- ✅ Enable SQLite encryption (e.g., SQLCipher)
- ✅ Regular backups with encryption
- ✅ Restrict database file permissions (0600)

## Dependency Security

We use several third-party dependencies. To check for vulnerabilities:

```bash
# Using pip-audit
pip install pip-audit
pip-audit

# Using safety
pip install safety
safety check
```

## Security Headers

When deploying in production, ensure these security headers are set:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
```

## Input Validation

The application implements:
- ✅ File type validation
- ✅ File size limits
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS protection
- ✅ CSRF protection (Flask-WTF recommended)

## Current Dependencies Security Status

Last checked: August 2026

| Package | Version | Status |
|---------|---------|--------|
| Flask | Latest | ✅ Secure |
| pandas | Latest | ✅ Secure |
| openpyxl | Latest | ✅ Secure |

Run `pip-audit` or `safety check` before deployment to verify current status.

## Vulnerability Disclosure Timeline

We aim to follow responsible disclosure practices:

1. **Day 0**: Receive report
2. **Day 1**: Initial acknowledgment
3. **Day 5**: Initial assessment provided
4. **Day 14**: Fix in progress or timeline provided
5. **Day 30**: Security update released
6. **Day 31**: Vulnerability disclosed publicly

## Security Updates

- Security updates will be released as soon as possible
- We will maintain security patches for at least 2 major versions
- Subscribe to release notifications for security updates

## Compliance

This project aims to comply with:
- OWASP Top 10
- CWE/SANS Top 25
- NIST Cybersecurity Framework recommendations

## Contact

- **Security Issues**: chirag.helpline16@example.com (mark subject with [SECURITY])
- **Other Issues**: Use GitHub Issues
- **General Inquiries**: chirag.helpline16@example.com

---

**Last Updated**: August 2026
**Version**: 1.0
