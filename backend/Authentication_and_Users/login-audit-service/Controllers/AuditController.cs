using Microsoft.AspNetCore.Mvc;
using login_audit_service.Models;
using login_audit_service.Services;
using System;
using System.Linq; 


namespace login_audit_service.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuditController : ControllerBase
    {
        private readonly DatabaseService _db;

        public AuditController(DatabaseService db)
        {
            _db = db;
        }

        [HttpPost]
        public IActionResult Log([FromBody] AuditRecord record)
        {
            record.AuditId = Guid.NewGuid().ToString();
            record.Timestamp = DateTime.UtcNow;

            _db.InsertAudit(record);
            return Ok(new { message = "Audit log stored." });
        }

        [HttpGet("{userId}")]
        public IActionResult Get(string userId)
        {
            var logs = _db.GetAudits(userId);
            if (!logs.Any()) return NotFound("No audit logs found.");
            return Ok(logs);
        }
    }
}
