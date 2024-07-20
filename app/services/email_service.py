class EmailService:
    def send_email(self, to, subject, body):
        # Implement email sending logic here
        return {'message': f'Email sent to {to}'}, 200
