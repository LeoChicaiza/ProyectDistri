using System;

namespace login_audit_service.Models
{
    public class AuditRecord
    {
        public string AuditId { get; set; }
        public string UserId { get; set; }
        public string Action { get; set; }
        public string Status { get; set; }
        public DateTime Timestamp { get; set; }
    }
}
