import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { BootstrapService } from './bootstrap.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService, BootstrapService],
})
export class AppModule {}
