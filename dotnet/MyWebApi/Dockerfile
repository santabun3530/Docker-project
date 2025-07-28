# Use the official .NET SDK image for building
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

# Copy everything and publish
COPY . ./
RUN dotnet publish -c Release -o out

# Use a smaller runtime image for running the app
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app/out .

EXPOSE 8080
ENTRYPOINT ["dotnet", "MyWebApi.dll"]
