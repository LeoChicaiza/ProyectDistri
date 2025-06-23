using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.AspNetCore.Hosting;
using login_audit_service.Services;
using Microsoft.Extensions.Configuration;

var builder = WebApplication.CreateBuilder(args);

// Leer configuración de appsettings.json 
builder.Configuration.AddJsonFile("appsettings.json", optional: false, reloadOnChange: true);

// Configura Kestrel para escuchar en el puerto 5000
builder.WebHost.ConfigureKestrel(serverOptions =>
{
    serverOptions.ListenAnyIP(5000);
});

// Agrega servicios
builder.Services.AddControllers();
builder.Services.AddSingleton<DatabaseService>(); 

var app = builder.Build();

app.UseRouting();
app.MapControllers();

app.Run();



