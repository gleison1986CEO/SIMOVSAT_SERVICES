
sqlcmd -S 1.tcp.sa.ngrok.io,20889 -U sa -P '0908Gle@' -C
sqlcmd -S 167.172.144.33 -U sa -P '0908Gle@gle28poker'
dotnet publish -c Release
CREATE USER gleison FOR LOGIN gleison
CREATE LOGIN gleison WITH PASSWORD = '0908Gle@gle28poker';
GRANT CREATE, EXECUTE, SELECT, INSERT, DELETE, UPDATE TO gleison WITH GRANT OPTION ;


DROP DATABASE atise
GO
CREATE DATABASE  atise
GO
USE atise
GO
SELECT * FROM INFORMATION_SCHEMA.TABLES 
SELECT * FROM Sys.Tables
GO


--CONFERE TABELAS
SELECT name FROM sys.tables
---QUERY ORGANIZADA SQLSERVER -------------------------------------------------------------------------------
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON

------------LOGIN ----------------------------------


IF OBJECT_ID(N'[__EFMigrationsHistory]') IS NULL BEGIN CREATE TABLE [__EFMigrationsHistory] ( [MigrationId] nvarchar(150) NOT NULL, [ProductVersion] nvarchar(32) NOT NULL, CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId]) ); END;
GO

BEGIN TRANSACTION;
GO

CREATE TABLE [AspNetRoles] ( [Id] nvarchar(450) NOT NULL, [Name] nvarchar(256) NULL, [NormalizedName] nvarchar(256) NULL, [ConcurrencyStamp] nvarchar(max) NULL, CONSTRAINT [PK_AspNetRoles] PRIMARY KEY ([Id]) );
GO

CREATE TABLE [AspNetUsers] ( [Id] nvarchar(450) NOT NULL, [UserName] nvarchar(256) NULL, [NormalizedUserName] nvarchar(256) NULL, [Email] nvarchar(256) NULL, [NormalizedEmail] nvarchar(256) NULL, [EmailConfirmed] bit NOT NULL, [PasswordHash] nvarchar(max) NULL, [SecurityStamp] nvarchar(max) NULL, [ConcurrencyStamp] nvarchar(max) NULL, [PhoneNumber] nvarchar(max) NULL, [PhoneNumberConfirmed] bit NOT NULL, [TwoFactorEnabled] bit NOT NULL, [LockoutEnd] datetimeoffset NULL,[LockoutEnabled] bit NOT NULL, [AccessFailedCount] int NOT NULL, CONSTRAINT [PK_AspNetUsers] PRIMARY KEY ([Id]));
GO

CREATE TABLE [AspNetRoleClaims] ( [Id] int NOT NULL IDENTITY, [RoleId] nvarchar(450) NOT NULL, [ClaimType] nvarchar(max) NULL, [ClaimValue] nvarchar(max) NULL, CONSTRAINT [PK_AspNetRoleClaims] PRIMARY KEY ([Id]), CONSTRAINT [FK_AspNetRoleClaims_AspNetRoles_RoleId] FOREIGN KEY ([RoleId]) REFERENCES [AspNetRoles] ([Id]) ON DELETE CASCADE );
GO

CREATE TABLE [AspNetUserClaims] ( [Id] int NOT NULL IDENTITY, [UserId] nvarchar(450) NOT NULL, [ClaimType] nvarchar(max) NULL, [ClaimValue] nvarchar(max) NULL, CONSTRAINT [PK_AspNetUserClaims] PRIMARY KEY ([Id]), CONSTRAINT [FK_AspNetUserClaims_AspNetUsers_UserId] FOREIGN KEY ([UserId]) REFERENCES [AspNetUsers] ([Id]) ON DELETE CASCADE);
GO

CREATE TABLE [AspNetUserLogins] ( [LoginProvider] nvarchar(128) NOT NULL, [ProviderKey] nvarchar(128) NOT NULL, [ProviderDisplayName] nvarchar(max) NULL, [UserId] nvarchar(450) NOT NULL, CONSTRAINT [PK_AspNetUserLogins] PRIMARY KEY ([LoginProvider], [ProviderKey]), CONSTRAINT [FK_AspNetUserLogins_AspNetUsers_UserId] FOREIGN KEY ([UserId]) REFERENCES [AspNetUsers] ([Id]) ON DELETE CASCADE );
GO

CREATE TABLE [AspNetUserRoles] ( [UserId] nvarchar(450) NOT NULL, [RoleId] nvarchar(450) NOT NULL, CONSTRAINT [PK_AspNetUserRoles] PRIMARY KEY ([UserId], [RoleId]), CONSTRAINT [FK_AspNetUserRoles_AspNetRoles_RoleId] FOREIGN KEY ([RoleId]) REFERENCES [AspNetRoles] ([Id]) ON DELETE CASCADE, CONSTRAINT [FK_AspNetUserRoles_AspNetUsers_UserId] FOREIGN KEY ([UserId]) REFERENCES [AspNetUsers] ([Id]) ON DELETE CASCADE );
GO

CREATE TABLE [AspNetUserTokens] ( [UserId] nvarchar(450) NOT NULL, [LoginProvider] nvarchar(128) NOT NULL, [Name] nvarchar(128) NOT NULL, [Value] nvarchar(max) NULL, CONSTRAINT [PK_AspNetUserTokens] PRIMARY KEY ([UserId], [LoginProvider], [Name]), CONSTRAINT [FK_AspNetUserTokens_AspNetUsers_UserId] FOREIGN KEY ([UserId]) REFERENCES [AspNetUsers] ([Id]) ON DELETE CASCADE );
GO

CREATE INDEX [IX_AspNetRoleClaims_RoleId] ON [AspNetRoleClaims] ([RoleId]);
GO

CREATE UNIQUE INDEX [RoleNameIndex] ON [AspNetRoles] ([NormalizedName]) WHERE [NormalizedName] IS NOT NULL;
GO

CREATE INDEX [IX_AspNetUserClaims_UserId] ON [AspNetUserClaims] ([UserId]);
GO

CREATE INDEX [IX_AspNetUserLogins_UserId] ON [AspNetUserLogins] ([UserId]);
GO

CREATE INDEX [IX_AspNetUserRoles_RoleId] ON [AspNetUserRoles] ([RoleId]);
GO

CREATE INDEX [EmailIndex] ON [AspNetUsers] ([NormalizedEmail]);
GO

CREATE UNIQUE INDEX [UserNameIndex] ON [AspNetUsers] ([NormalizedUserName]) WHERE [NormalizedUserName] IS NOT NULL;
GO

INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion]) VALUES (N'20230905213832_advocacia', N'6.0.21');
GO

COMMIT;
GO

------------- LOGIN ---------------------------------------


------------ ALTER TABLES ---------------------------------


ALTER TABLE [dbo].[AspNetRoleClaims]  WITH CHECK ADD  CONSTRAINT [FK_AspNetRoleClaims_AspNetRoles_RoleId] FOREIGN KEY([RoleId])REFERENCES [dbo].[AspNetRoles] ([Id])ON DELETE CASCADE
GO




ALTER TABLE [dbo].[AspNetRoleClaims] CHECK CONSTRAINT [FK_AspNetRoleClaims_AspNetRoles_RoleId]
GO




ALTER TABLE [dbo].[AspNetUserClaims]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserClaims_AspNetUsers_UserId] FOREIGN KEY([UserId])REFERENCES [dbo].[AspNetUsers] ([Id])ON DELETE CASCADE
GO




ALTER TABLE [dbo].[AspNetUserClaims] CHECK CONSTRAINT [FK_AspNetUserClaims_AspNetUsers_UserId]
GO




ALTER TABLE [dbo].[AspNetUserLogins] WITH CHECK ADD CONSTRAINT [FK_AspNetUserLogins_AspNetUsers_UserId] FOREIGN KEY([UserId]) REFERENCES [dbo].[AspNetUsers] ([Id]) ON DELETE CASCADE
GO




ALTER TABLE [dbo].[AspNetUserLogins] CHECK CONSTRAINT [FK_AspNetUserLogins_AspNetUsers_UserId]
GO




ALTER TABLE [dbo].[AspNetUserRoles]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserRoles_AspNetRoles_RoleId] FOREIGN KEY([RoleId])REFERENCES [dbo].[AspNetRoles] ([Id])ON DELETE CASCADE
GO



ALTER TABLE [dbo].[AspNetUserRoles] CHECK CONSTRAINT [FK_AspNetUserRoles_AspNetRoles_RoleId]
GO



ALTER TABLE [dbo].[AspNetUserRoles]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserRoles_AspNetUsers_UserId] FOREIGN KEY([UserId])REFERENCES [dbo].[AspNetUsers] ([Id])ON DELETE CASCADE
GO



ALTER TABLE [dbo].[AspNetUserRoles] CHECK CONSTRAINT [FK_AspNetUserRoles_AspNetUsers_UserId]
GO




ALTER TABLE [dbo].[AspNetUserTokens]  WITH CHECK ADD  CONSTRAINT [FK_AspNetUserTokens_AspNetUsers_UserId] FOREIGN KEY([UserId])REFERENCES [dbo].[AspNetUsers] ([Id])ON DELETE CASCADE
GO




ALTER TABLE [dbo].[AspNetUserTokens] CHECK CONSTRAINT [FK_AspNetUserTokens_AspNetUsers_UserId]
GO


------------ ALTER TABLES ---------------------------------

------------ TABLES FOR USE ON LAUDOS ---------------------



CREATE TABLE [dbo].[Tokens]([codigo] [int] IDENTITY(1,1) NOT NULL,[Token] [nvarchar](1250) NULL,[Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO

CREATE TABLE [dbo].[ConexaUser]([codigo] [int] IDENTITY(1,1) NOT NULL, [situacao] [nvarchar](1250) NULL, [name] [nvarchar](1250) NULL, [date] [nvarchar](1250) NULL, [cpf] [nvarchar](250) NULL, [agenda]  [nvarchar](450) NULL, [email] [nvarchar](450) NULL, [especialidade] [nvarchar](450) NULL,  [telefone] [nvarchar](1250) NULL, [Ativo] [bit] NULL,  PRIMARY KEY CLUSTERED ([codigo] ASC), UNIQUE (cpf) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY] 
GO

CREATE TABLE [dbo].[ClubeUser]([codigo] [int] IDENTITY(1,1) NOT NULL, [situacao] [nvarchar](1250) NULL,  [name] [nvarchar](1250) NULL, [date] [nvarchar](1250) NULL, [cpf] [nvarchar](250) NULL, [agenda]  [nvarchar](450) NULL, [email] [nvarchar](450) NULL, [especialidade] [nvarchar](450) NULL,  [telefone] [nvarchar](1250) NULL, [Ativo] [bit] NULL,  PRIMARY KEY CLUSTERED ([codigo] ASC), UNIQUE (cpf) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY] 
GO

CREATE TABLE [dbo].[Users]([codigo] [int] IDENTITY(1,1) NOT NULL, [codigo_associado] [nvarchar](1250) NULL, [tipo] [nvarchar](1250) NULL, [cpf] [nvarchar](1250) NULL, [rg]  [nvarchar](250) NULL, [email] [nvarchar](250) NULL,  [whastapp] [nvarchar](1250) NULL, [cnh] [nvarchar](1250) NULL, [descricao] [nvarchar](1250) NULL,[Ativo] [bit] NULL,  PRIMARY KEY CLUSTERED ([codigo] ASC), CONSTRAINT rg_associado UNIQUE (rg, email) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY] 
GO

CREATE TABLE [dbo].[Vehicles]([codigo] [int] IDENTITY(1,1) NOT NULL,[codigo_veiculo] [nvarchar](1250) NULL, [placa] [nvarchar](1250) NULL, [chassi] [nvarchar](1250) NULL, [renavam] [nvarchar](1250) NULL, [codigo_associado] [nvarchar](1250) NULL, [codigo_tipo] [nvarchar](1250) NULL, [codigo_categoria] [nvarchar](1250) NULL, [tipo] [nvarchar](1250) NULL, [categoria] [nvarchar](1250) NULL, [marca] [nvarchar](1250) NULL, [modelo] [nvarchar](1250) NULL, [cpf] [nvarchar](250) NULL, [rg] [nvarchar](250) NULL, [email] [nvarchar](1250) NULL, [codigo_situacao] [nvarchar](1250) NULL, [codigo_voluntario] [nvarchar](1250) NULL, [nome_associado] [nvarchar](1250) NULL, [whatsapp] [nvarchar](1250) NULL, [Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC), CONSTRAINT rg UNIQUE (rg, cpf) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Locations]([codigo] [int] IDENTITY(1,1) NOT NULL, [imei] [nvarchar](1250) NULL, [rastreador] [nvarchar](1250) NULL, [latitude] [nvarchar](1250) NULL, [longitude] [nvarchar](1250) NULL, [dateGps] [nvarchar](1250) NULL, [altitude] [nvarchar](1250) NULL, [bateria] [nvarchar](1250) NULL, [protocol] [nvarchar](1250) NULL, [lastPosition] [nvarchar](1250) NULL, [nome] [nvarchar](1250) NULL, [telefone] [nvarchar](1250) NULL, [cpf] [nvarchar](250) NULL, [registro] [nvarchar](1250) NULL, [proprietario] [nvarchar](1250) NULL, [tabela_fipe] [nvarchar](1250) NULL, [dados_veiculo] [nvarchar](1250) NULL, [placa] [nvarchar](1250) NULL, [batery] [nvarchar](1250) NULL, [totaldistance] [nvarchar](1250) NULL, [motion] [nvarchar](1250) NULL, [ignition] [nvarchar](1250) NULL, [charge] [nvarchar](1250) NULL, [blocked] [nvarchar](1250) NULL, [Ativo] [bit] NULL, PRIMARY KEY CLUSTERED ([codigo] ASC), CONSTRAINT cpf UNIQUE (cpf)  WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO


CREATE TABLE [dbo].[Cooperativas]([codigo] [int] IDENTITY(1,1) NOT NULL,[codigo_cooperativa] [nvarchar](1250) NULL,[nome] [nvarchar](1250) NULL,[valor_pagamento] [nvarchar](1250) NULL,[logradouro] [nvarchar](1250) NULL,[numero] [nvarchar](1250) NULL,[complemento] [nvarchar](1250) NULL,[bairro] [nvarchar](1250) NULL,[cidade] [nvarchar](1250) NULL,[estado] [nvarchar](1250) NULL,[cep] [nvarchar](1250) NULL,[email] [nvarchar](250) NULL,[cpf] [nvarchar](250) NULL,[contato] [nvarchar](1250) NULL,[telefone] [nvarchar](1250) NULL,[valor_pagamento_residual] [nvarchar](1250) NULL,[telefone_comercial] [nvarchar](1250) NULL,[formato_pagamento_residual] [nvarchar](1250) NULL,[formato_pagamento] [nvarchar](1250) NULL,[situacao] [nvarchar](1250) NULL,[Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC), CONSTRAINT codigo UNIQUE (cpf, email) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO

         
CREATE TABLE [dbo].[Produto]([codigo] [int] IDENTITY(1,1) NOT NULL,[codigo_produto] [nvarchar](1250) NULL,[decricao_produto] [nvarchar](1250) NULL,[valor_produto] [nvarchar](1250) NULL,[valor_fipe_inicial] [nvarchar](1250) NULL,[codigo_classificacao_produto] [nvarchar](1250) NULL,[compulsorio] [nvarchar](1250) NULL,[formato_cobranca] [nvarchar](1250) NULL,[codigo_tipo_veiculo] [nvarchar](1250) NULL,[descricao_tipo_veiculo] [nvarchar](1250) NULL,[regionais_cod] [nvarchar](1250) NULL,[regionais_name] [nvarchar](1250) NULL,[Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO
      

CREATE TABLE [dbo].[Regionais]([codigo] [int] IDENTITY(1,1)NOT NULL,[codigo_regional] [nvarchar](1250) NULL,[nome] [nvarchar](1250) NULL,[nome_fantasia] [nvarchar](1250) NULL,[cnpj] [nvarchar](1250) NULL,[logradouro] [nvarchar](1250) NULL,[numero] [nvarchar](1250) NULL,[complemento] [nvarchar](1250) NULL,[bairro] [nvarchar](1250) NULL,[cidade] [nvarchar](1250) NULL,[estado] [nvarchar](1250) NULL,[cep] [nvarchar](1250) NULL,[email] [nvarchar](1250) NULL,[website] [nvarchar](1250) NULL,[telefone] [nvarchar](1250) NULL, [situacao] [nvarchar](1250) NULL,[Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO    


CREATE TABLE [dbo].[Situacao]([codigo] [int] IDENTITY(1,1) NOT NULL, [codigo_situacao] [nvarchar](1250) NULL, [descricao_situacao] [nvarchar](1250) NULL, [situacao] [nvarchar](1250) NULL, [Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO


CREATE TABLE [dbo].[Voluntarios]([codigo] [int] IDENTITY(1,1) NOT NULL,[codigo_voluntario] [nvarchar](1250) NULL,[nome] [nvarchar](1250) NULL,[cpf] [nvarchar](250) NULL,[telefone] [nvarchar](1250) NULL,[telefone_comercial] [nvarchar](1250) NULL,[cep] [nvarchar](1250) NULL,[celular] [nvarchar](1250) NULL,[email] [nvarchar](250) NULL,[situacao] [nvarchar](1250) NULL,[formato_pagamento] [nvarchar](1250) NULL,[valor_pagamento] [nvarchar](1250) NULL,[formato_pagamento_residual] [nvarchar](1250) NULL,[codigo_classificacao] [nvarchar](1250) NULL,[valor_pagamento_residual] [nvarchar](1250) NULL,[obs] [nvarchar](1250) NULL,[logradouro] [nvarchar](1250) NULL,[numero] [nvarchar](1250) NULL,[complemento] [nvarchar](1250) NULL,[bairro] [nvarchar](1250) NULL,[cidade] [nvarchar](1250) NULL,[estado] [nvarchar](1250) NULL,[Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC), UNIQUE (cpf, email)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO


CREATE TABLE [dbo].[Infornet]([codigo] [int] IDENTITY(1,1) NOT NULL, [name] [nvarchar](1250) NULL, [cpf] [nvarchar](250) NULL, [Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC),UNIQUE (cpf)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Historico]([codigo] [int] IDENTITY(1,1) NOT NULL, [nome] [nvarchar](1250) NULL, [tipo] [nvarchar](1250) NULL, [descricao] [nvarchar](1250) NULL, [data] [nvarchar](250) NULL, [Ativo] [bit] NULL,PRIMARY KEY CLUSTERED ([codigo] ASC)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS= ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]) ON [PRIMARY]
GO


------------ PROCEDURES --------------------------------------------------------------


------------ SELECT ------------------------------------------------------------------

CREATE PROCEDURE sp_grau  AS SELECT codigo, nome, Ativo FROM dbo.grau ;
GO


------------ INSERT ------------------------------------------------------------------

CREATE PROCEDURE sp_cadastrar_grau  @nome NVARCHAR(250) = NULL, @hashcode NVARCHAR(250) = NULL, @data_hora NVARCHAR(250) = NULL, @Ativo  NVARCHAR(50) = NULL AS BEGIN  INSERT INTO dbo.grau (nome, Ativo)VALUES(@nome, @Ativo)  INSERT INTO dbo.hash (hash_login, data_hora)VALUES(@hashcode, @data_hora) END 
GO



 
 ------------ UPDATE ------------------------------------------------------------------



CREATE PROCEDURE sp_atualizar_cidades  @codigo NVARCHAR(250) =  NULL, @hashcode NVARCHAR(250) =  NULL,  @data_hora NVARCHAR(250) =  NULL ,   @cargo NVARCHAR(250)=  NULL, @login NVARCHAR(250)=  NULL, @executou NVARCHAR(250)=  NULL,              @nome NVARCHAR(250) = NULL,  @latitude NVARCHAR(250) =  NULL, @longitude NVARCHAR(250) =  NULL, @Ativo  NVARCHAR(50) = NULL AS BEGIN                 UPDATE dbo.cidade set @codigo = codigo, nome = @nome, lat = @latitude, long = @longitude, Ativo = @Ativo where codigo=@codigo                             INSERT INTO dbo.datalog (hashcode, data_hora, cargo, login, executou)VALUES(@hashcode, @data_hora, @cargo, @login, @executou)   END
GO

-------------------------DELETE ------------------------

CREATE PROCEDURE sp_cidade_delete  @codigo NVARCHAR(250) = NULL AS  DELETE FROM dbo.cidade where codigo = @codigo
GO


--------------  search


----------------------------------SET QUOTED_IDENTIFIER -------------------------------------
SET QUOTED_IDENTIFIER ON
GO
----------------------------------SET QUOTED_IDENTIFIER -------------------------------------

----------------------------------SET ANSI_NULLS ON------------------------------------------
SET ANSI_NULLS ON
GO
----------------------------------SET ANSI_NULLS ON------------------------------------------


------------------------------///////////////////////////////////////////////////////////////////////////////////////////////////////
INSERT INTO dbo.AspNetUsers(Id,UserName,NormalizedUserName,Email,NormalizedEmail,EmailConfirmed,PasswordHash,SecurityStamp,ConcurrencyStamp,PhoneNumber,PhoneNumberConfirmed,TwoFactorEnabled,LockoutEnd,LockoutEnabled,AccessFailedCount)VALUES('b5ef2f06-cfca-42f8-9979-e69434a57480','Gleison','GLEISON','lionmonkeydesignapp@gmail.com','lionmonkeydesignapp@gmail.com',0,'AQAAAAEAACcQAAAAEKxguH2LBhaJsDUHJ88VMhRXh1MzYDTdmiWsfFYqCjCA3aZ3EMSsjCqHkHmcxmAo7g==','L2FLOHN5K5AICZXAGL4C7TP7SID6E5AU','0fc55b05-b405-45aa-9b75-5ce013ef1120','',0,0,'',1,0);
GO
INSERT INTO dbo.AspNetRoles(Id,Name,NormalizedName,ConcurrencyStamp)VALUES('60cd773b-3b13-4f3-a2cd-af35e8f1352c','Administrador','ADMINISTRADOR','2856098f-0219-4e15-a-769-294e60e2a6b4');
GO
INSERT INTO dbo.AspNetUserRoles(UserId,RoleId)VALUES('b5ef2f06-cfca-42f8-9979-e69434a57480','60cd773b-3b13-4f3-a2cd-af35e8f1352c');
GO
------------------------------///////////////////////////////////////////////////////////////////////////////////////////////////////