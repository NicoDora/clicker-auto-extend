import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { BootstrapService } from './bootstrap.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigModule } from '@nestjs/config';

@Module({
  imports: [
    ConfigModule.forRoot(),
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: process.env.MYSQL_HOST,
      port: parseInt(process.env.MYSQL_PORT),
      username: process.env.MYSQL_USER,
      password: process.env.MYSQL_PASSWORD,
      database: process.env.MYSQL_NAME,
      synchronize: true,
      logging: true,
      entities: ['dist/**/entities/*{.ts,.js}'],
    }),
  ],
  controllers: [AppController],
  providers: [AppService, BootstrapService],
})
export class AppModule {}
