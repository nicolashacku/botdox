import requests
import os
import json
import discord
from discord.ext import commands
import re
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
sol_res = 128
api1 = 8
api2 = 0
api3 = 0
api4 = 0
api5= 0
api6 =0
api7 =0
api8  = 0
api9 = 0
#https://pastebin.com/raw/GZPEU63h
#https://pastebin.com/raw/YV77G3yQ
#https://pastebin.com/raw/3qDWsxFi
#
@bot.command(case_insensitive=True)
async def nombres(ctx, tipo=None, numero=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7 ,api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1=api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2=api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3=api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4=api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5=api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6=api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7=api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8=api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9=api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    else:
        sol_res= sol_res-1
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
            embed.add_field(name=f'Nombre Completo',
                            value=f'{fullName}', inline=False)
            embed.add_field(name=f'Nombres', value=f'{firstName}', inline=True)
            embed.add_field(name=f'Apellido', value=f'{lastName}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes', value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


@bot.command(case_insensitive=True)
async def vehiculo(ctx, tipo=None, numero=None, placa=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7 ,api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1=api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2=api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3=api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4=api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5=api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6=api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7=api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8=api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9=api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE, TI, PA, RC")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    elif placa == None:
        await ctx.send("Debe digitar la placa del vehiculo XXXXXX")
    else:
        sol_res=sol_res-1
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
            embed.add_field(name=f'activacion',
                            value=f'{activacion}', inline=True)
            embed.add_field(name=f'status', value=f'{status}', inline=True)
            embed.add_field(name=f'numero SOAT',
                            value=f'{numeroSoat}', inline=True)
            embed.add_field(name=f'Expedicion Soat',
                            value=f'{expedicionSoat}', inline=True)
            embed.add_field(name=f'Vencimiento Soat',
                            value=f'{vecimientoSoat}', inline=True)
            embed.add_field(name=f'Tecnomecanica',
                            value=f'{tecnomecanica}', inline=True)
            embed.add_field(name=f'Numero Tecnomecanica',
                            value=f'{numeroTecno}', inline=True)
            embed.add_field(name=f'Expedicion Tecno',
                            value=f'{expedicionTecno}', inline=True)
            embed.add_field(name=f'Vencimiento Tecno',
                            value=f'{vencimientoTecno}', inline=True)
            #embed.add_field(name=f'Tipo Servicio', value =f'{tipoServicio}',inline=True)
            #embed.add_field(name=f'Numero Motor', value =f'{numMotor}',inline=True)
            #embed.add_field(name=f'Numero chasis', value =f'{numChasis}',inline=True)
            #embed.add_field(name=f'Cilindraje', value =f'{cilindraje}',inline=True)
            #embed.add_field(name=f'Limite ocupantes', value =f'{ocupantes}',inline=True)
            embed.add_field(name=f'Solicitudes Restantes', value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


@bot.command()
async def conductor(ctx, tipo=None, numero=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7 ,api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1=api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2=api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3=api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4=api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5=api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6=api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7=api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8=api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9=api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    else:
        sol_res=sol_res-1
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
                x=0
                for i in words:
                    if x == 1:
                        numeroLic = i
                        numeroLic = re.sub("\'|\,","",numeroLic)
                    if x == 9:
                        status = i
                        status = re.sub("\'|\,","",status)
                    x=x+1

            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            embed.add_field(name=f'Nombre Completo',
                            value=f'{fullName}', inline=False)
            embed.add_field(name=f'Total de licencias',
                            value=f'{totalLicencias}', inline=True)
            #embed.add_field(name=f'Numero licencia', value =f'{numeroLicencia}',inline=True)
            #embed.add_field(name=f'Estado licencia', value =f'{statusLicencias}',inline=True)
            #embed.add_field(name=f'Vencimiento licencia', value =f'{vencimientoLicencia}',inline=True)
            embed.add_field(name=f'Paz y Salvo',
                            value=f'{pazandSafe}', inline=True)
            embed.add_field(name=f'Numero paz y salvo',
                            value=f'{pazNumber}', inline=True)
            embed.add_field(name=f'Numero de impuestos',
                            value=f'{transitTaxesNumber}', inline=True)
            embed.add_field(name=f'Numero de suspensiones',
                            value=f'{suspensiones}', inline=True)
            embed.add_field(name=f'Numero De Licencia', value=f'{numeroLic}', inline=False)
            embed.add_field(name=f'Status Licencia', value=f'{status}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes', value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


@bot.command()
async def afiliaciones(ctx, tipo=None, numero=None, fecha=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7 ,api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1=api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2=api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3=api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4=api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5=api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6=api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7=api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8=api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9=api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, PA, CE, PEP, TI.")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    elif fecha == None:
        await ctx.send("Debe digitar una fecha de nacimiento")
    else:
        sol_res = sol_res -1
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
            fechaCorte = j['data']['informacionPersonal']['fechaCorte']
            primerNombre = j['data']['informacionPersonal']['primerNombre']
            segundoNombre = j['data']['informacionPersonal']['segundoNombre']
            primerApellido = j['data']['informacionPersonal']['primerApellido']
            segundoApellido = j['data']['informacionPersonal']['segundoApellido']
            sexo = j['data']['informacionPersonal']['sexo']
            eps = j['data']['eps']['eps']
            regimen = j['data']['eps']['regimen']
            fechaAfiliacion = j['data']['eps']['fechaAfiliacion']
            estadoAfiliacion = j['data']['eps']['estadoAfiliacion']
            fechaAfiliacion = j['data']['eps']['fechaAfiliacion']
            tipoAfiliado = j['data']['eps']['tipoAfiliado']
            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            embed.add_field(name=f'Fecha corte',
                            value=f'{fechaCorte}', inline=False)
            embed.add_field(name=f'Primer nombre',
                            value=f'{primerNombre}', inline=True)
            embed.add_field(name=f'Segundo Nombre',
                            value=f'{segundoNombre}', inline=True)
            embed.add_field(name=f'Primer apellido',
                            value=f'{primerApellido}', inline=True)
            embed.add_field(name=f'Segundo apellido',
                            value=f'{segundoApellido}', inline=True)
            embed.add_field(name=f'sexo', value=f'{sexo}', inline=False)
            embed.add_field(name=f'Eps', value=f'{eps}', inline=True)
            embed.add_field(name=f'Regimen', value=f'{regimen}', inline=True)
            embed.add_field(name=f'Fecha afiliacion',
                            value=f'{fechaAfiliacion}', inline=False)
            embed.add_field(name=f'Estado afiliacion',
                            value=f'{estadoAfiliacion}', inline=False)
            embed.add_field(name=f'Fecha afiliacion',
                            value=f'{fechaAfiliacion}', inline=True)
            embed.add_field(name=f'Tipo Afiliado',
                            value=f'{tipoAfiliado}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes', value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)


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
    global sol_res, api1, api2, api3, api4, api5, api6, api7 ,api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1=api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2=api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3=api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4=api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5=api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6=api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7=api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8=api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9=api9+1
    key = a
    if placa == None:
        await ctx.send("Debe introducir una placa XXXXXX")
    else:
        sol_res=sol_res-1
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
            placa = j['data']['vehiculo']['placa']
            modelo = j['data']['vehiculo']['modelo']
            numeroChasis = j['data']['vehiculo']['numeroChasis']
            marca = j['data']['vehiculo']['marca']
            linea = j['data']['vehiculo']['linea']
            claseVehiculo = j['data']['vehiculo']['claseVehiculo']
            #tipoDoc = j['data']['propietarios']['tipoDocumento']
            #noDocumento = j['data']['propietarios']
            #nombreCompleto = j['data']['propietarios']['nombreCompleto']
            doc = json.loads(response.text)
            a = doc['data']['propietarios']
            b = str(a)
            words = b.split()
            x=0
            for i in words:
                if x == 15:
                    primerNombre = i
                    primerNombre = re.sub("\'|\,","",primerNombre)
                if x == 19:
                    primerApellido = i
                    primerApellido = re.sub("\'|\,","",primerApellido)
                if x == 21:
                    segundoApellido = i
                    segundoApellido = re.sub("\'|\,","",segundoApellido)
                if x == 8:
                    numeroDoc = i
                    numeroDoc = re.sub("\'|\,","",numeroDoc)
                x=x+1

            embed = discord.Embed(
                colour=discord.Colour.blue()

            )
            embed.add_field(name=f'PLaca',
                            value=f'{placa}', inline=False)
            embed.add_field(name=f'Modelo',
                            value=f'{modelo}', inline=True)
            embed.add_field(name=f'Numero Chasis',
                            value=f'{numeroChasis}', inline=True)
            embed.add_field(name=f'Marca',
                            value=f'{marca}', inline=True)
            embed.add_field(name=f'Linea',
                            value=f'{linea}', inline=True)
            embed.add_field(name=f'Clase Vehiculo', value=f'{claseVehiculo}', inline=True)
            embed.add_field(name=f'Numero Documento', value=f'{numeroDoc}', inline=False)
            embed.add_field(name=f'Primer Nombre', value=f'{primerNombre}', inline=True)
            embed.add_field(name=f'Primer Apellido', value=f'{primerApellido}', inline=True)
            embed.add_field(name=f'Segundo Apellido', value=f'{segundoApellido}', inline=True)
            embed.add_field(name=f'Solicitudes Restantes', value=f'{sol_res}', inline=False)
            embed.set_footer(
                text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)

@bot.command(case_insensitive=True)
async def placaperu(ctx, tipo=None, numero=None, placa=None):
    global sol_res, api1, api2, api3, api4, api5, api6, api7 ,api8, api9
    if api1 < 15:
        request1 = requests.get("https://pastebin.com/raw/JgrikEEF")
        a = request1.text
        api1=api1+1
    elif api2 < 15:
        request1 = requests.get("https://pastebin.com/raw/P1JCUPDb")
        a = request1.text
        api2=api2+1
    elif api3 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api3=api3+1
    elif api4 < 15:
        request1 = requests.get("https://pastebin.com/raw/cdGBJ396")
        a = request1.text
        api4=api4+1
    elif api5 < 15:
        request1 = requests.get("https://pastebin.com/raw/2VQNYEqe")
        a = request1.text
        api5=api5+1
    elif api6 < 15:
        request1 = requests.get("https://pastebin.com/raw/uK2Mcbys")
        a = request1.text
        api6=api6+1
    elif api7 < 15:
        request1 = requests.get("https://pastebin.com/raw/0QbWu5AA")
        a = request1.text
        api7=api7+1
    elif api8 < 15:
        request1 = requests.get("https://pastebin.com/raw/iCC44qHk")
        a = request1.text
        api8=api8+1
    elif api9 < 15:
        request1 = requests.get("https://pastebin.com/raw/MPvHRrSm")
        a = request1.text
        api9=api9+1
    key = a
    if tipo == None:
        await ctx.send("Debe digitar una placa")
    else:
        sol_res=sol_res-1
        
bot.run(os.environ['DISCORD_TOKEN'])
