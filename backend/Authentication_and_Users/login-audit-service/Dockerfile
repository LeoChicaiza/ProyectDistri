# FASE 1 – SDK para compilar
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src

# 1) Copiamos sólo el csproj
COPY login-audit-service.csproj ./

# 2) Restauramos paquetes
RUN dotnet restore "./login-audit-service.csproj"

# 3) Copiamos sólo el código de este servicio
COPY . . 

# 4) Publicamos
RUN dotnet publish "./login-audit-service.csproj" -c Release -o /app/publish

# FASE 2 – Runtime
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish ./
EXPOSE 5000
ENTRYPOINT ["dotnet", "login-audit-service.dll"]

