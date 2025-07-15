using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace HealthCheckClient
{
    class Program
    {
        static async Task Main()
        {
            // Apunta al puerto 5000 donde corre tu servicio
            var client = new HttpClient { BaseAddress = new Uri("http://localhost:5000") };

            try
            {
                // Petición al endpoint de salud
                var res = await client.GetAsync("/health");
                var body = await res.Content.ReadAsStringAsync();
                var json = JsonDocument.Parse(body).RootElement;

                if (res.IsSuccessStatusCode && json.GetProperty("status").GetString() == "ok")
                {
                    Console.WriteLine("Health OK");
                    Environment.Exit(0);
                }
                else
                {
                    Console.WriteLine($"Health FAILED: {res.StatusCode} - {body}");
                    Environment.Exit(1);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Exception: {ex.Message}");
                Environment.Exit(1);
            }
        }
    }
}


