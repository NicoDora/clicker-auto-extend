import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { BootstrapService } from './bootstrap.service';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const bootstrapService = app.get(BootstrapService);

  await bootstrapService.setStartingServer(app);
}
bootstrap();
