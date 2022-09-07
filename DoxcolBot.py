import requests
import os
import json
import discord
from discord.ext import commands
import re
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
sol_res = 61
api1 = 15
api2 = 15
api3 = 15
api4 = 15
api5 = 15
api6 = 12
api7 = 0
api8 = 0
api9 = 0
# https://pastebin.com/raw/GZPEU63h
# https://pastebin.com/raw/YV77G3yQ
# https://pastebin.com/raw/3qDWsxFi
#


@bot.command(case_insensitive=True)
async def nombres(ctx, tipo=None, numero=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7, api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1 = api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2 = api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3 = api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4 = api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5 = api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6 = api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7 = api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8 = api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9 = api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    else:
        sol_res = sol_res-1
        url = f"https://api.verifik.co/v2/co/cedula?documentType={tipo}&documentNumber={numero}"
        payload = {}
        headers = {
            'Authorization': f'JWT {key}'
        }
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            fullName = j['data']['fullName']
            firstName = j['data']['firstName']
            lastName = j['data']['lastName']
            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            embed.add_field(name=f'Nombre Completo',value=f'{fullName}', inline=False)
            embed.add_field(name=f'Nombres', value=f'{firstName}', inline=True)
            embed.add_field(name=f'Apellido', value=f'{lastName}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes',value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


@bot.command(case_insensitive=True)
async def vehiculo(ctx, tipo=None, numero=None, placa=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7, api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1 = api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2 = api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3 = api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4 = api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5 = api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6 = api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7 = api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8 = api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9 = api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE, TI, PA, RC")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    elif placa == None:
        await ctx.send("Debe digitar la placa del vehiculo XXXXXX")
    else:
        sol_res = sol_res-1
        url = f"https://api.verifik.co/v2/co/runt/vehiculo?documentType={tipo}&documentNumber={numero}&plate={placa}"
        payload = {}
        headers = {
            'Authorization': f'JWT {key}'
        }
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            placa = j['data']['plate']
            color = j['data']['vehicleInformation']['color']
            marca = j['data']['vehicleInformation']['brand']
            activacion = j['data']['vehicleInformation']['enrollmentDate']
            status = j['data']['vehicleInformation']['status']
            numeroSoat = j['data']['soat']['soatNumber']
            expedicionSoat = j['data']['soat']['expeditionDate']
            vecimientoSoat = j['data']['soat']['dueDate']
            tecnomecanica = j['data']['techReview']['valid']
            numeroTecno = j['data']['techReview']['reviewNumber']
            expedicionTecno = j['data']['techReview']['valid']
            vencimientoTecno = j['data']['techReview']['dueDate']
            response2 = requests.get(
                f"https://api.verifik.co/v2/co/runt/vehiculo-completo?plate={placa}")
            #j2 = response2.json()
            #tipoServicio = j2['data']['vehicle']['tipoServicio']
            ##numMotor = j2['data']['vehicle']['noMotor']
            #numChasis = j2['data']['vehicle']['noChasis']
            #cilindraje = j2['data']['vehicle']['1000']
            #ocupantes = j2['data']['vehicle']['ocupantes']

            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            embed.add_field(name=f'placa', value=f'{placa}', inline=False)
            embed.add_field(name=f'color', value=f'{color}', inline=True)
            embed.add_field(name=f'marca', value=f'{marca}', inline=True)
            embed.add_field(name=f'activacion',value=f'{activacion}', inline=True)
            embed.add_field(name=f'status', value=f'{status}', inline=True)
            embed.add_field(name=f'numero SOAT',value=f'{numeroSoat}', inline=True)
            embed.add_field(name=f'Expedicion Soat',value=f'{expedicionSoat}', inline=True)
            embed.add_field(name=f'Vencimiento Soat',value=f'{vecimientoSoat}', inline=True)
            embed.add_field(name=f'Tecnomecanica',value=f'{tecnomecanica}', inline=True)
            embed.add_field(name=f'Numero Tecnomecanica',value=f'{numeroTecno}', inline=True)
            embed.add_field(name=f'Expedicion Tecno',value=f'{expedicionTecno}', inline=True)
            embed.add_field(name=f'Vencimiento Tecno',value=f'{vencimientoTecno}', inline=True)
            #embed.add_field(name=f'Tipo Servicio', value =f'{tipoServicio}',inline=True)
            #embed.add_field(name=f'Numero Motor', value =f'{numMotor}',inline=True)
            #embed.add_field(name=f'Numero chasis', value =f'{numChasis}',inline=True)
            #embed.add_field(name=f'Cilindraje', value =f'{cilindraje}',inline=True)
            #embed.add_field(name=f'Limite ocupantes', value =f'{ocupantes}',inline=True)
            embed.add_field(name=f'Solicitudes Restantes',value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


@bot.command()
async def conductor(ctx, tipo=None, numero=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7, api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1 = api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2 = api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3 = api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4 = api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5 = api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6 = api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7 = api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8 = api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9 = api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    else:
        sol_res = sol_res-1
        url = f"https://api.verifik.co/v2/co/runt/consultarConductor?documentType={tipo}&documentNumber={numero}"
        payload = {}
        headers = {
            'Authorization': f'JWT {key}'
        }
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            fullName = j['data']['fullName']
            totalLicencias = j['data']['totallicencias']
            #numeroLicencia = j['data']['licencias']['licenceNumber']
            #statusLicencias = j['data']['licencias']['status']
            #vencimientoLicencia = j['data']['licencias']['dueDate']
            pazandSafe = j['data']['transitTaxes']['paceAndSafe']
            pazNumber = j['data']['transitTaxes']['paceAndSafeNumber']
            transitTaxesNumber = j['data']['transitTaxes']['transitTaxesNumber']
            suspensiones = j['data']['transitTaxes']['suspensionDate']
            if "licencias" in response.text:
                example = json.loads(response.text)
                a = example['data']['licencias']
                b = str(a)
                words = b.split()
                x = 0
                for i in words:
                    if x == 1:
                        numeroLic = i
                        numeroLic = re.sub("\'|\,", "", numeroLic)
                    if x == 9:
                        status = i
                        status = re.sub("\'|\,", "", status)
                    x = x+1

            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            embed.add_field(name=f'Nombre Completo',value=f'{fullName}', inline=False)
            embed.add_field(name=f'Total de licencias',value=f'{totalLicencias}', inline=True)
            #embed.add_field(name=f'Numero licencia', value =f'{numeroLicencia}',inline=True)
            #embed.add_field(name=f'Estado licencia', value =f'{statusLicencias}',inline=True)
            #embed.add_field(name=f'Vencimiento licencia', value =f'{vencimientoLicencia}',inline=True)
            embed.add_field(name=f'Paz y Salvo',value=f'{pazandSafe}', inline=True)
            embed.add_field(name=f'Numero paz y salvo',value=f'{pazNumber}', inline=True)
            embed.add_field(name=f'Numero de impuestos',value=f'{transitTaxesNumber}', inline=True)
            embed.add_field(name=f'Numero de suspensiones',value=f'{suspensiones}', inline=True)
            embed.add_field(name=f'Numero De Licencia',value=f'{numeroLic}', inline=False)
            embed.add_field(name=f'Status Licencia',value=f'{status}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes',value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


@bot.command()
async def afiliaciones(ctx, tipo=None, numero=None, fecha=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7, api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1 = api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2 = api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3 = api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4 = api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5 = api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6 = api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7 = api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8 = api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9 = api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, PA, CE, PEP, TI.")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    elif fecha == None:
        await ctx.send("Debe digitar una fecha de nacimiento")
    else:
        sol_res = sol_res - 1
        url = f"https://api.verifik.co/v2/co/afiliaciones?documentType={tipo}&documentNumber={numero}&date={fecha}"
        payload = {}
        headers = {
            'Authorization': f'JWT {key}'
        }
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            class Persona:
                def __init__(self):
                    self.fechaDeCorte = j['data']['informacionPersonal']['fechaCorte']
                    self.firstName = j['data']['informacionPersonal']['primerNombre']
                    self.secondName = j['data']['informacionPersonal']['segundoNombre']
                    self.lastName = j['data']['informacionPersonal']['primerApellido']
                    self.secondLastName = j['data']['informacionPersonal']['segundoApellido']
                    self.sexo = j['data']['informacionPersonal']['sexo']
                    self.eps = j['data']['eps']['eps']
                    self.regimen = j['data']['eps']['regimen']
                    self.FechaAfiliacion = j['data']['eps']['fechaAfiliacion']
                    self.EstadoAfiliacion = j['data']['eps']['estadoAfiliacion']
                    self.tipoDeAfiliacion = j['data']['eps']['tipoAfiliado']
            persona = Persona()
            embed.add_field(name=f'Fecha corte',value=f'{persona.fechaDeCorte}', inline=False)
            embed.add_field(name=f'Primer nombre',value=f'{persona.firstName}', inline=True)
            embed.add_field(name=f'Segundo Nombre',value=f'{persona.secondName}', inline=True)
            embed.add_field(name=f'Primer apellido',value=f'{persona.lastName}', inline=True)
            embed.add_field(name=f'Segundo apellido',value=f'{persona.secondLastName}', inline=True)
            embed.add_field(name=f'Sexo',value=f'{persona.sexo}', inline=False)
            embed.add_field(name=f'Eps', value=f'{persona.eps}', inline=True)
            embed.add_field(name=f'Regimen',value=f'{persona.regimen}', inline=True)
            embed.add_field(name=f'Fecha afiliacion',value=f'{persona.FechaAfiliacion}', inline=False)
            embed.add_field(name=f'Estado afiliacion',value=f'{persona.EstadoAfiliacion}', inline=False)
            embed.add_field(name=f'Fecha afiliacion',value=f'{persona.FechaAfiliacion}', inline=True)
            embed.add_field(name=f'Tipo Afiliado',value=f'{persona.tipoDeAfiliacion}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes',value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)

@bot.command()
async def apisstatus(ctx):
    await ctx.send(f"{api1},{api2},{api3},{api4},{api5},{api6},{api7},{api8},{api9}")
@bot.command()
async def comandos(ctx):
    global sol_res
    embed = discord.Embed(
        title='DoxColBot',
        description='Desarrolado por nicolas.5301\n https://instagram.com/nicolas.5301',
        colour=discord.Colour.blue()

    )
    embed.add_field(name='>nombres',
                    value='Consulta el nombre por su CC, CE', inline=False)
    embed.add_field(
        name='>vehiculo', value='Da toda la informacion del vehiculo con el numero de documento y placa', inline=False)
    embed.add_field(name='>conductor',
                    value='nombres del conductor por CC, CE', inline=False)
    embed.add_field(name='>afiliaciones',
                    value='Consulta eps y afliaciones, uso >afilaciones tipo_doc numero_doc fecha_nacmiento', inline=False)
    embed.add_field(
        name='>placa', value='Consulta infromacion por la placa', inline=False)
    embed.add_field(
        name='>solicitudes', value='Muestra cuantas solictudes le qudan al bot', inline=False)
    embed.add_field(name=">apisstatus", value="Muestra cuantas solis le queda a cada api", inline=False)
    embed.add_field(name=">verificar",value="Te cambia el numero al operador virgin mobile tienes que ingresar el numero sin el +57")

    await ctx.send(embed=embed)


@bot.command()
async def solicitudes(ctx):
    global sol_res
    await ctx.send(f"Le quedan {sol_res}/150 solictudes restantes")


@bot.command()
async def borrar(ctx):
    await ctx.channel.purge(limit=None)


@bot.command()
async def placa(ctx, placa=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7, api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1 = api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2 = api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3 = api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4 = api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5 = api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6 = api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7 = api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8 = api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9 = api9+1
    key = a
    if placa == None:
        await ctx.send("Debe introducir una placa XXXXXX")
    else:
        sol_res = sol_res-1
        url = f"https://api.verifik.co/v2/co/soat/consultarVehiculo?plate={placa}"
        payload = {}
        headers = {
            'Authorization': f'JWT {key}'
        }
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            doc = json.loads(response.text)
            a = doc['data']['propietarios']
            b = str(a)
            words = b.split()
            x = 0
            for i in words:
                if x == 15:
                    primerNombre = i
                    primerNombre = re.sub("\'|\,", "", primerNombre)
                if x == 19:
                    primerApellido = i
                    primerApellido = re.sub("\'|\,", "", primerApellido)
                if x == 21:
                    segundoApellido = i
                    segundoApellido = re.sub("\'|\,", "", segundoApellido)
                if x == 8:
                    numeroDoc = i
                    numeroDoc = re.sub("\'|\,", "", numeroDoc)
                x = x+1
            class Carro:       
                def __init__(self):
                    self.numeroPlaca = j['data']['vehiculo']['placa']
                    self.modeloCarro = j['data']['vehiculo']['modelo']
                    self.numeroDelChasis = j['data']['vehiculo']['numeroChasis']
                    self.marcaCarro = j['data']['vehiculo']['marca']
                    self.lineaCarro = j['data']['vehiculo']['linea']
                    self.ClaseDelCarro = j['data']['vehiculo']['claseVehiculo']
                    self.numeroDocumento = numeroDoc
                    self.primerNombrePropietario = primerNombre
                    self.primerApellidoPropietario = primerApellido
                    self.segundoApellidoPropietario = segundoApellido
            embed = discord.Embed(
                colour=discord.Colour.blue()
            )
            carro = Carro()
            embed.add_field(name=f'Placa',value=f'{carro.numeroPlaca}', inline=False)
            embed.add_field(name=f'Modelo',value=f'{carro.modeloCarro}', inline=True)
            embed.add_field(name=f'Numero Chasis',value=f'{carro.numeroDelChasis}', inline=True)
            embed.add_field(name=f'Marca',value=f'{carro.marcaCarro}', inline=True)
            embed.add_field(name=f'Linea',value=f'{carro.lineaCarro}', inline=True)
            embed.add_field(name=f'Clase Vehiculo',value=f'{carro.ClaseDelCarro}', inline=True)
            embed.add_field(name=f'Numero Documento',value=f'{carro.numeroDocumento}', inline=False)
            embed.add_field(name=f'Primer Nombre',value=f'{carro.primerNombrePropietario}', inline=True)
            embed.add_field(name=f'Primer Apellido',value=f'{carro.primerApellidoPropietario}', inline=True)
            embed.add_field(name=f'Segundo Apellido',value=f'{carro.segundoApellidoPropietario}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes',value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)
@bot.command()
async def tullave(ctx, numero=None):
    if numero == None:
        await ctx.send("Debe digitar el numero de tarjeta...")
    else:
        url = "https://tmsa-transmiapp-shvpc.uc.r.appspot.com/lectura_tarjeta"
        payload = {
            "numero_tarjeta":f"{numero}",
            "consultar":"true"
        }
        headers = {
            'Content-Type':'application/json'
        }
        response = requests.post(url,headers=headers,json=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o el numero de tarjeta es invalido.")
        else:
            words = str(json.loads(response.text)).split()
            x=0
            for i in words:
                if x == 1:
                    numeroTarjeta = i
                    numeroTarjeta = re.sub("\'|\,", "", numeroTarjeta)
                elif x == 3:
                    saldoTarjeta = i
                    saldoTarjeta = re.sub("\'|,","",saldoTarjeta)
                x=x+1
            embed = discord.Embed(
                colour = discord.Colour.blue()
            )
            embed.add_field(name=f'Numero De Tarjeta:',value=f'{numeroTarjeta}', inline=False)
            embed.add_field(name=f'Saldo De La Tarjeta',value=f'{saldoTarjeta}', inline=True)
            embed.set_footer(text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)
@bot.command()
async def verificar(ctx, numero=None):
    url='https://app.virginmobile.co/api/evident/sms-evident'
    if numero == None or len(numero) < 10:
        await ctx.send("Debe digitar un numero valido")
    else:
        _headers = {"Content-Type": "application/json"}
        _json = {"phoneNumber":f"{numero}","brand":{"id":1},"channel":{"id":5},"message":"Â¡Jelou! usa {code} como codigo de verificacion para tu linea. :)"}
        response = requests.post(url,headers=_headers,data=json.dumps(_json))
        j = response.json()
        status = j['success']
        codigo = j['data']['code']
        embed = discord.Embed(
                colour=discord.Colour.blue()
        )
        embed.add_field(name="Estado", value=f"{status}")
        embed.add_field(name="Codigo para verificarse",value=f"{codigo}")
        await ctx.send(embed=embed)

bot.run(os.environ['DISCORD_TOKEN'])
