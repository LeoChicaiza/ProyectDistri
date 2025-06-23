using Npgsql;
using login_audit_service.Models;
using System;
using Microsoft.Extensions.Configuration; 
using System.Collections.Generic;        



namespace login_audit_service.Services
{
    public class DatabaseService
    {
        private readonly string _connectionString;

        public DatabaseService(IConfiguration config)
        {
            _connectionString = config.GetConnectionString("PostgresConnection");
        }

        public void InsertAudit(AuditRecord record)
        {
            using var conn = new NpgsqlConnection(_connectionString);
            conn.Open();

            var cmd = new NpgsqlCommand(
                "INSERT INTO login_audits (audit_id, user_id, action, status, timestamp) VALUES (@id, @user, @action, @status, @timestamp)", conn);

            cmd.Parameters.AddWithValue("id", record.AuditId);
            cmd.Parameters.AddWithValue("user", record.UserId ?? (object)DBNull.Value);
            cmd.Parameters.AddWithValue("action", record.Action);
            cmd.Parameters.AddWithValue("status", record.Status);
            cmd.Parameters.AddWithValue("timestamp", record.Timestamp);

            cmd.ExecuteNonQuery();
        }

        public List<AuditRecord> GetAudits(string userId)
        {
            var audits = new List<AuditRecord>();
            using var conn = new NpgsqlConnection(_connectionString);
            conn.Open();

            var cmd = new NpgsqlCommand("SELECT * FROM login_audits WHERE user_id = @user", conn);
            cmd.Parameters.AddWithValue("user", userId);
            using var reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                audits.Add(new AuditRecord
                {
                    AuditId = reader["audit_id"].ToString(),
                    UserId = reader["user_id"].ToString(),
                    Action = reader["action"].ToString(),
                    Status = reader["status"].ToString(),
                    Timestamp = DateTime.Parse(reader["timestamp"].ToString())
                });
            }

            return audits;
        }
    }
}
